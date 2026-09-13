#!/usr/bin/env python3
"""Jenkins 全量 job/folder 入图导入器（CMDB，Neo4j via `jc neo4j`）。

把 new-jenkins.jereh.cn 的只读快照 `~/.jereh-cli/jenkins-inventory.json`
（`jc jenkins` Groovy Script Console 生成，READ-ONLY，不触发任何构建）
建成知识图谱，与 import_resreg.py 建好的 :GB10 数字孪生子图打通。

数据源（只读，绝不触发构建）:
  ~/.jereh-cli/jenkins-inventory.json
    {server, generatedAt, jobCount, lastBuildResultSummary, notes[], jobs[]}
    每个 job: {name(含 folder/ 路径), shortName, type(pipeline|freestyle),
              rawType, params[], purpose, description,
              lastBuild:{number,result,ts,ts_epoch_ms,building}}
  文件夹（Folder）从 job 的 `name` 中的 `/` 路径推导（快照未单列 folder 实体）。

本体（节点标签，均附带 :GB10 标记标签 + :Jenkins 便于整体清理/重建；source 属性统一 jenkins-inventory）:
  JenkinsServer / Folder / JenkinsJob

关系:
  (JenkinsServer)-[:HAS_FOLDER]->(Folder)        顶层文件夹
  (Folder)-[:HAS_FOLDER]->(Folder)               嵌套文件夹（如 ecb/dcim）
  (JenkinsServer)-[:HAS_JOB]->(JenkinsJob)       顶层 job（无文件夹）
  (Folder)-[:HAS_JOB]->(JenkinsJob)              文件夹内 job
  (TestLine)-[:USES_JOB]->(JenkinsJob)           测试线/资源引用了 job（与 resreg 打通）
  (Worktree)-[:BUILT_BY]->(JenkinsJob)           worktree 所属仓库由某 job 构建/发布

节点属性（JenkinsJob）:
  fullName(含路径) / name(shortName) / type / lastResult / lastBuildNumber
  / lastBuildTime(ISO) / building / url / purpose
  —— 绝不写入任何 token/JWT/密码（快照本身也不含凭据；params 只存名字与说明，
     doc-manager-build 的 DEPLOY_JWT 只是参数「定义」，无实际值）。

安全纪律:
  - READ-ONLY：只读快照文件，绝不调用 jc jenkins build trigger / buildWithParameters。
  - 密码/JWT 值绝不入图：只存 job 元数据（名称/结果/时间/URL），不存 params 的 default 值
    （避免把 GIT_REPO 之类的默认串或任何潜在敏感串带入；只记录参数名清单）。
  - 所有 Cypher 走参数化，杜绝注入。
  - 幂等：先删本子图（:Jenkins 标记）再重建。

用法:
    python3 scripts/import_jenkins.py            # 读快照 + 全量刷新 Jenkins 子图
    python3 scripts/import_jenkins.py --dry-run  # 只打印将写入的节点/关系，不落库
    python3 scripts/import_jenkins.py --stats    # 导入后打印统计（默认也会打印）
    python3 scripts/import_jenkins.py --inventory <path>  # 指定快照文件

依赖: `jc neo4j`（HTTP Query API），凭据见 `jc env`。
"""

import argparse
import json
import subprocess
from pathlib import Path

HOME = Path.home()
INVENTORY = HOME / ".jereh-cli" / "jenkins-inventory.json"
MARKER = "GB10"        # 与 import_resreg.py 同一数字孪生子图标记，便于跨源关联查询
JMARK = "Jenkins"      # Jenkins 子图专用标记，本脚本只清理/重建带此标记的节点
JC_TIMEOUT = 55        # 每条命令 <= 60s 纪律

# resreg owner/worktree -> 关联的 Jenkins job/folder（人工映射，基于 shell-discipline + resreg 语义）
# DSH IDE 门户线（deepseek-harness/ide）对应 dsh 文件夹的发布 job 与 doc-manager-build 部署 job。
TESTLINE_JOB_LINKS = [
    # (testline_owner, job_fullName)
    ("门户e2e线", "dsh/ide-portal-publish"),
    ("门户e2e线", "dsh/ide-portal-deploy"),
    ("全旅程验收线", "doc-manager-build"),
    ("冒烟修复线", "doc-manager-build"),
]
# worktree 路径片段 -> 由某 job 构建/发布
WORKTREE_JOB_LINKS = [
    # (worktree_path_substring, job_fullName)
    ("deepseek-harness/ide", "dsh/ide-portal-publish"),
]


# --------------------------- 底层：jc neo4j 调用 ---------------------------

def cypher(statement: str, params: dict | None = None) -> dict:
    cmd = ["jc", "neo4j", "query", "--cypher", statement]
    if params:
        cmd += ["--params", json.dumps(params, ensure_ascii=False)]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=JC_TIMEOUT)
    except subprocess.TimeoutExpired:
        raise SystemExit(f"[FATAL] jc neo4j 超时(>{JC_TIMEOUT}s)：{statement[:60]}...")
    if out.returncode != 0:
        raise SystemExit(f"[FATAL] jc neo4j 失败: {out.stderr or out.stdout}")
    try:
        resp = json.loads(out.stdout)
    except json.JSONDecodeError:
        raise SystemExit(f"[FATAL] 无法解析 jc neo4j 输出: {out.stdout[:200]}")
    if not resp.get("success", False):
        raise SystemExit(f"[FATAL] Cypher 报错: {resp.get('message') or resp}")
    return resp.get("data", {})


# --------------------------- MERGE 助手 ---------------------------

def merge_node(dry, primary_label, key_prop, key_val, props: dict):
    props = {k: v for k, v in props.items() if v not in (None, "")}
    set_clause = ", ".join(f"n.{k} = ${k}" for k in props)
    stmt = f"MERGE (n:{primary_label}:{MARKER}:{JMARK} {{{key_prop}: $__key}})"
    if set_clause:
        stmt += f" SET {set_clause}"
    params = {"__key": key_val, **props}
    if dry:
        print(f"[DRY] NODE {primary_label} {key_prop}={key_val} {props}")
        return
    cypher(stmt, params)


def merge_rel(dry, a_label, a_key, a_val, rel, b_label, b_key, b_val,
              a_marker=None, b_marker=None):
    """建关系。a_marker/b_marker 允许连到非 :Jenkins 的既有 :GB10 节点（如 TestLine/Worktree）。"""
    al = f"{a_label}:{a_marker}" if a_marker else f"{a_label}:{MARKER}:{JMARK}"
    bl = f"{b_label}:{b_marker}" if b_marker else f"{b_label}:{MARKER}:{JMARK}"
    stmt = (f"MATCH (a:{al} {{{a_key}: $a}}), (b:{bl} {{{b_key}: $b}}) "
            f"MERGE (a)-[:{rel}]->(b)")
    if dry:
        print(f"[DRY] REL ({a_label} {a_val})-[:{rel}]->({b_label} {b_val})")
        return
    cypher(stmt, {"a": a_val, "b": b_val})


# --------------------------- 采集：快照解析 ---------------------------

def load_inventory(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"[FATAL] 未找到 Jenkins 快照: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def folder_prefixes(fullname: str) -> list[str]:
    """从 job fullName 推导其所有祖先文件夹路径。

    注意：Jenkins multibranch 分支名可能被 URL-encode（如 contract%2Fdcim），
    其中的 %2F 是分支名里的 '/'，不是文件夹分隔符。这里按未编码的 '/' 切分，
    对 %2F 不拆分（它属于叶子 job 名的一部分）。
    """
    parts = fullname.split("/")
    # 最后一段是 job 自身；其余是文件夹链
    prefixes = []
    for i in range(1, len(parts)):
        prefixes.append("/".join(parts[:i]))
    return prefixes


# --------------------------- 建图 ---------------------------

def wipe(dry: bool):
    """只清 Jenkins 子图（带 :Jenkins 标记），不动 resreg/repo/container 的 :GB10 节点。"""
    stmt = f"MATCH (n:{JMARK}) DETACH DELETE n"
    if dry:
        print(f"[DRY] {stmt}")
        return
    cypher(stmt)


def build(dry: bool, inv: dict):
    server = inv.get("server", "https://new-jenkins.jereh.cn")
    jobs = inv.get("jobs", [])

    # --- Server 根节点 ---
    merge_node(dry, "JenkinsServer", "url", server, {
        "name": server.replace("https://", "").replace("http://", "").rstrip("/"),
        "jobCount": inv.get("jobCount"),
        "generatedAt": inv.get("generatedAt"),
        "source": "jenkins-inventory",
    })

    # --- 文件夹（从 job 路径推导），建立嵌套 HAS_FOLDER ---
    all_folders: set[str] = set()
    for j in jobs:
        for pref in folder_prefixes(j.get("name", "")):
            all_folders.add(pref)
    for folder in sorted(all_folders):
        merge_node(dry, "Folder", "fullName", folder, {
            "name": folder.split("/")[-1],
            "source": "jenkins-inventory",
        })
    # 连边：顶层文件夹 <- Server；嵌套文件夹 <- 父文件夹
    for folder in sorted(all_folders):
        if "/" in folder:
            parent = folder.rsplit("/", 1)[0]
            merge_rel(dry, "Folder", "fullName", parent, "HAS_FOLDER",
                      "Folder", "fullName", folder)
        else:
            merge_rel(dry, "JenkinsServer", "url", server, "HAS_FOLDER",
                      "Folder", "fullName", folder)

    # --- Jobs ---
    n_jobs = 0
    for j in jobs:
        fullname = j.get("name", "")
        if not fullname:
            continue
        lb = j.get("lastBuild") or {}
        # 构造 job URL（Jenkins 每层用 /job/ 分隔；分支名里的 %2F 保持不动）
        url_path = "/".join(f"job/{seg}" for seg in fullname.split("/"))
        job_url = f"{server.rstrip('/')}/{url_path}/"
        merge_node(dry, "JenkinsJob", "fullName", fullname, {
            "name": j.get("shortName", fullname.split("/")[-1]),
            "type": j.get("type"),
            "purpose": j.get("purpose"),
            "paramNames": ",".join(p.get("name", "") for p in (j.get("params") or [])) or None,
            "lastResult": lb.get("result"),
            "lastBuildNumber": lb.get("number"),
            "lastBuildTime": lb.get("ts"),
            "building": lb.get("building"),
            "url": job_url,
            "source": "jenkins-inventory",
        })
        n_jobs += 1
        # 归属：有文件夹则连文件夹，否则连 Server
        if "/" in fullname:
            parent = fullname.rsplit("/", 1)[0]
            merge_rel(dry, "Folder", "fullName", parent, "HAS_JOB",
                      "JenkinsJob", "fullName", fullname)
        else:
            merge_rel(dry, "JenkinsServer", "url", server, "HAS_JOB",
                      "JenkinsJob", "fullName", fullname)

    # --- 与既有 resreg :GB10 子图打通（TestLine / Worktree 引用 Jenkins job） ---
    job_names = {j.get("name") for j in jobs}
    linked = 0
    for owner, job_full in TESTLINE_JOB_LINKS:
        if job_full in job_names:
            # TestLine 节点由 import_resreg.py 建（:TestLine:GB10，无 :Jenkins）
            merge_rel(dry, "TestLine", "name", owner, "USES_JOB",
                      "JenkinsJob", "fullName", job_full,
                      a_marker=MARKER)  # a 侧用既有 :GB10，不要求 :Jenkins
            linked += 1
    # worktree -> job（按路径片段模糊匹配既有 Worktree 节点）
    wt_linked = 0
    if not dry:
        for sub, job_full in WORKTREE_JOB_LINKS:
            if job_full not in job_names:
                continue
            # 找到匹配的 worktree 节点，逐个建边
            data = cypher(
                f"MATCH (w:Worktree:{MARKER}) WHERE w.path CONTAINS $sub "
                f"MATCH (j:JenkinsJob:{JMARK} {{fullName:$job}}) "
                f"MERGE (w)-[:BUILT_BY]->(j) RETURN count(w) AS c",
                {"sub": sub, "job": job_full})
            wt_linked += data["records"][0]["c"] if data.get("records") else 0
    else:
        for sub, job_full in WORKTREE_JOB_LINKS:
            print(f"[DRY] REL (Worktree ~{sub})-[:BUILT_BY]->(JenkinsJob {job_full})")

    return {"folders": len(all_folders), "jobs": n_jobs,
            "testline_links": linked, "worktree_links": wt_linked, "server": server}


def print_stats():
    data = cypher(
        f"MATCH (n:{JMARK}) WITH labels(n) AS ls "
        f"UNWIND ls AS l WITH l WHERE l <> '{MARKER}' AND l <> '{JMARK}' "
        f"RETURN l AS label, count(*) AS c ORDER BY c DESC")
    total_n = cypher(f"MATCH (n:{JMARK}) RETURN count(n) AS c")["records"][0]["c"]
    total_r = cypher(
        f"MATCH (a:{JMARK})-[r]->(b) RETURN count(r) AS c")["records"][0]["c"]
    res = cypher(
        f"MATCH (n:{JMARK}:JenkinsJob) WITH n.lastResult AS r "
        f"RETURN coalesce(r,'NEVER_BUILT') AS result, count(*) AS c ORDER BY c DESC")
    print("\n=== Jenkins CMDB 子图统计 ===")
    print(f"Jenkins 节点: {total_n}   关系(含跨子图): {total_r}")
    print("按标签:")
    for rec in data["records"]:
        print(f"  {rec['label']}: {rec['c']}")
    print("job 最近构建结果分布:")
    for rec in res["records"]:
        print(f"  {rec['result']}: {rec['c']}")


def main():
    ap = argparse.ArgumentParser(description="Jenkins 全量 job/folder 入图导入器（CMDB）")
    ap.add_argument("--dry-run", action="store_true", help="只打印将写入的节点/关系，不落库")
    ap.add_argument("--stats", action="store_true", help="导入后打印统计（默认即打印）")
    ap.add_argument("--no-wipe", action="store_true", help="不清空 Jenkins 子图（增量 MERGE）")
    ap.add_argument("--inventory", default=str(INVENTORY), help="Jenkins 快照 JSON 路径")
    args = ap.parse_args()

    inv = load_inventory(Path(args.inventory))
    print(f"读取快照: server={inv.get('server')} jobCount={inv.get('jobCount')} "
          f"generatedAt={inv.get('generatedAt')}")

    if not args.dry_run and not args.no_wipe:
        print("清空旧 :Jenkins 子图 ...")
    if not args.no_wipe:
        wipe(args.dry_run)

    counts = build(args.dry_run, inv)
    print(f"入图: folders={counts['folders']}, jobs={counts['jobs']}, "
          f"testline链接={counts['testline_links']}, worktree链接={counts['worktree_links']}")

    if not args.dry_run:
        print_stats()


if __name__ == "__main__":
    main()
