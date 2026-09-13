#!/usr/bin/env python3
"""GB10 服务器数字孪生知识图谱导入器（Neo4j via `jc neo4j`）。

把这台开发主机（GB10）的**资源与业务实体**建成可持续查询的知识图谱。
数据源全部为本机实时状态，每次运行即为一次「快照刷新」（幂等：先清本子图再重建）。

实体源:
  ① resreg 资源注册表  ~/.jereh-cli/resource-registry.json
     -> 端口(Port) / worktree(Worktree) / 目录(Directory)，含 owner(测试线) / purpose
  ② 仓库拓扑           ~/repo/github.com/**, ~/repo/jc/**, ~/wt/**
     -> 仓库(Repo) / 分支(Branch) / worktree 归属（git rev-parse）
  ③ 容器拓扑           docker ps + VIRTUAL_HOST
     -> 应用容器(Container) / 域名(Domain)

本体（节点标签，均附带 :GB10 标记标签 + source 属性，便于整体清理/重建）:
  Host / TestLine / Port / Worktree / Directory / ChromeInstance / Repo / Branch
  / Container / Domain

关系:
  (TestLine)-[:OCCUPIES]->(Port|Directory)      占用（resreg claim）
  (TestLine)-[:OWNS]->(Worktree)                拥有 worktree
  (Worktree)-[:BELONGS_TO]->(Repo)              worktree 归属仓库
  (Worktree)-[:ON_BRANCH]->(Branch)             worktree 当前分支
  (Repo)-[:HAS_BRANCH]->(Branch)                仓库分支
  (ChromeInstance)-[:LISTENS_ON]->(Port)        Chrome 实例监听 CDP 端口
  (ChromeInstance)-[:SERVES]->(TestLine)        实例服务于测试线
  (ChromeInstance)-[:USES_PROFILE]->(Directory) 实例使用 user-data-dir
  (Container)-[:DEPLOYED_AT]->(Domain)          应用部署在子域名
  (Container|Port|Worktree|Directory)-[:RUNS_ON]->(Host)  归属本机

安全纪律:
  - 密码/凭据值**绝不入图**：只存引用名（如 profile 目录名、owner 名），
    Neo4j 连接凭据由 `jc env`（NEO4J_BASE_URL/_USERNAME/_PASSWORD）提供，本脚本不读取明文。
  - 所有 Cypher 走参数化（--params），杜绝注入。

用法:
    python3 scripts/import_resreg.py            # 采集本机状态 + 全量刷新图
    python3 scripts/import_resreg.py --dry-run  # 只打印将要写入的节点/关系，不落库
    python3 scripts/import_resreg.py --stats    # 导入后打印图统计（默认也会打印）

依赖: `jc neo4j`（HTTP Query API），凭据见 `jc env`。
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

HOME = Path.home()
REGISTRY = HOME / ".jereh-cli" / "resource-registry.json"
REPO_BASES = [HOME / "repo" / "github.com", HOME / "repo" / "jc"]
WT_BASE = HOME / "wt"
HOST_NAME = "GB10"
MARKER = "GB10"  # 标记标签：本数字孪生子图统一挂 :GB10，便于整体清理/重建
JC_TIMEOUT = 55  # 每条命令 <= 60s 纪律


# --------------------------- 底层：jc neo4j 调用 ---------------------------

def cypher(statement: str, params: dict | None = None) -> dict:
    """执行一条参数化 Cypher，返回 jc neo4j 的 data 部分。"""
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


# --------------------------- 采集：三个数据源 ---------------------------

def load_registry() -> list[dict]:
    """读 resreg 注册表 claims。"""
    if not REGISTRY.exists():
        print(f"[WARN] 未找到 {REGISTRY}，跳过 resreg 源")
        return []
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return data.get("claims", [])


def git(path: Path, *args: str) -> str:
    try:
        out = subprocess.run(["git", "-C", str(path), *args],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        return ""


def discover_repos() -> list[dict]:
    """扫描仓库拓扑：主仓库 + worktree，识别归属与分支。"""
    seen: dict[str, dict] = {}
    candidates: list[Path] = []
    for base in REPO_BASES:
        if not base.exists():
            continue
        # 一层与两层（github.com/{org}/{repo}）
        for d in base.iterdir():
            if d.is_dir():
                candidates.append(d)
                for sub in d.iterdir():
                    if sub.is_dir():
                        candidates.append(sub)
    if WT_BASE.exists():
        for root, dirs, _files in os.walk(WT_BASE):
            p = Path(root)
            if (p / ".git").exists():
                candidates.append(p)
                dirs[:] = []  # 命中 worktree 后不再深入

    repos = []
    for d in candidates:
        git_marker = d / ".git"
        if not git_marker.exists():
            continue
        branch = git(d, "rev-parse", "--abbrev-ref", "HEAD")
        if not branch:
            continue
        remote = git(d, "config", "--get", "remote.origin.url")
        common = git(d, "rev-parse", "--git-common-dir")
        # git-common-dir 是相对/绝对；worktree 的 common-dir 指向主仓库的 .git
        is_worktree = git_marker.is_file()  # worktree 的 .git 是文件而非目录
        # 主仓库路径（用于归属）：common dir 的父目录
        common_path = Path(common)
        if not common_path.is_absolute():
            common_path = (d / common_path).resolve()
        main_repo = str(common_path.parent)
        # 仓库逻辑名：优先 remote 末段，否则目录名
        if remote:
            repo_name = remote.rstrip("/").split("/")[-1].removesuffix(".git")
        else:
            repo_name = Path(main_repo).name
        rec = {
            "path": str(d),
            "branch": branch,
            "remote": remote,
            "repo_name": repo_name,
            "main_repo": main_repo,
            "is_worktree": is_worktree,
        }
        if rec["path"] not in seen:
            seen[rec["path"]] = rec
            repos.append(rec)
    return repos


def discover_containers() -> list[dict]:
    """docker ps + VIRTUAL_HOST => 应用容器与域名。"""
    try:
        names = subprocess.run(["docker", "ps", "--format", "{{.Names}}"],
                               capture_output=True, text=True, timeout=15)
    except Exception as e:
        print(f"[WARN] docker 不可用，跳过容器源: {e}")
        return []
    if names.returncode != 0:
        print("[WARN] docker ps 失败，跳过容器源")
        return []
    result = []
    for name in names.stdout.split():
        insp = subprocess.run(
            ["docker", "inspect", name, "--format",
             "{{.Config.Image}}||{{range .Config.Env}}{{println .}}{{end}}"],
            capture_output=True, text=True, timeout=15)
        if insp.returncode != 0:
            continue
        image, _, env_blob = insp.stdout.partition("||")
        vhost = ""
        vport = ""
        for line in env_blob.splitlines():
            if line.startswith("VIRTUAL_HOST="):
                vhost = line.split("=", 1)[1].strip()
            elif line.startswith("VIRTUAL_PORT="):
                vport = line.split("=", 1)[1].strip()
        result.append({"name": name, "image": image.strip(),
                       "vhost": vhost, "vport": vport})
    return result


# --------------------------- 建图 ---------------------------

def wipe(dry: bool):
    """清除本数字孪生子图（只删 :GB10 标记的节点及其关系）。"""
    stmt = f"MATCH (n:{MARKER}) DETACH DELETE n"
    if dry:
        print(f"[DRY] {stmt}")
        return
    cypher(stmt)


def merge_node(dry, primary_label, key_prop, key_val, props: dict):
    """MERGE 一个节点：主标签 + :GB10 标记 + 属性。"""
    props = {k: v for k, v in props.items() if v not in (None, "")}
    set_clause = ", ".join(f"n.{k} = ${k}" for k in props)
    stmt = f"MERGE (n:{primary_label}:{MARKER} {{{key_prop}: $__key}})"
    if set_clause:
        stmt += f" SET {set_clause}"
    params = {"__key": key_val, **props}
    if dry:
        print(f"[DRY] NODE {primary_label} {key_prop}={key_val} {props}")
        return
    cypher(stmt, params)


def merge_rel(dry, a_label, a_key, a_val, rel, b_label, b_key, b_val):
    stmt = (f"MATCH (a:{a_label}:{MARKER} {{{a_key}: $a}}), "
            f"(b:{b_label}:{MARKER} {{{b_key}: $b}}) "
            f"MERGE (a)-[:{rel}]->(b)")
    if dry:
        print(f"[DRY] REL ({a_label} {a_val})-[:{rel}]->({b_label} {b_val})")
        return
    cypher(stmt, {"a": a_val, "b": b_val})


def build(dry: bool):
    claims = load_registry()
    repos = discover_repos()
    containers = discover_containers()

    # --- Host 根节点 ---
    merge_node(dry, "Host", "name", HOST_NAME,
               {"desc": "GB10 开发主机", "source": "static"})

    # --- resreg claims：Port / Directory / Worktree + TestLine(owner) ---
    testlines = set()
    port_owner = {}   # port value -> owner（供 Chrome 实例 SERVES 推断）
    for c in claims:
        owner = c.get("owner", "unknown")
        testlines.add(owner)
        merge_node(dry, "TestLine", "name", owner,
                   {"source": "resreg"})
        merge_rel(dry, "TestLine", "name", owner, "RUNS_ON", "Host", "name", HOST_NAME)

        ctype = c.get("type")
        val = c.get("value")
        purpose = c.get("purpose", "")
        if ctype == "port":
            merge_node(dry, "Port", "value", val,
                       {"purpose": purpose, "source": "resreg"})
            merge_rel(dry, "TestLine", "name", owner, "OCCUPIES", "Port", "value", val)
            merge_rel(dry, "Port", "value", val, "RUNS_ON", "Host", "name", HOST_NAME)
            port_owner[val] = owner
        elif ctype == "dir":
            merge_node(dry, "Directory", "path", val,
                       {"purpose": purpose, "source": "resreg"})
            merge_rel(dry, "TestLine", "name", owner, "OCCUPIES", "Directory", "path", val)
            merge_rel(dry, "Directory", "path", val, "RUNS_ON", "Host", "name", HOST_NAME)
        elif ctype == "worktree":
            merge_node(dry, "Worktree", "path", val,
                       {"purpose": purpose, "source": "resreg"})
            merge_rel(dry, "TestLine", "name", owner, "OWNS", "Worktree", "path", val)
            merge_rel(dry, "Worktree", "path", val, "RUNS_ON", "Host", "name", HOST_NAME)

    # --- Chrome 实例（规范约定的 3 条线 -> 端口 + profile 目录） ---
    # 依据 shell-discipline 实例分配表，端口即 CDP 端口，profile 是 user-data-dir。
    chrome_map = [
        {"port": "9222", "profile": "/tmp/iam-headed", "line": "冒烟修复线"},
        {"port": "9224", "profile": "/home/jereh/user-data-dir/9224", "line": "门户e2e线"},
        {"port": "9333", "profile": "/home/jereh/user-data-dir/9333", "line": "legacy"},
    ]
    for ch in chrome_map:
        inst = f"chrome:{ch['port']}"
        merge_node(dry, "ChromeInstance", "name", inst,
                   {"cdp_port": ch["port"], "profile": ch["profile"], "source": "shell-discipline"})
        merge_rel(dry, "ChromeInstance", "name", inst, "RUNS_ON", "Host", "name", HOST_NAME)
        # 监听端口（若该端口已在 resreg 建过节点则连上）
        if ch["port"] in port_owner or True:
            merge_node(dry, "Port", "value", ch["port"], {"source": "resreg"})
            merge_rel(dry, "ChromeInstance", "name", inst, "LISTENS_ON", "Port", "value", ch["port"])
        # profile 目录
        merge_node(dry, "Directory", "path", ch["profile"], {"source": "shell-discipline"})
        merge_rel(dry, "ChromeInstance", "name", inst, "USES_PROFILE", "Directory", "path", ch["profile"])
        # 服务的测试线
        owner = port_owner.get(ch["port"], ch["line"])
        merge_node(dry, "TestLine", "name", owner, {"source": "resreg"})
        merge_rel(dry, "ChromeInstance", "name", inst, "SERVES", "TestLine", "name", owner)

    # --- 仓库拓扑：Repo / Branch / Worktree 归属 ---
    # 先建主仓库集合
    main_repo_of = {}  # main_repo path -> repo_name
    for r in repos:
        main_repo_of[r["main_repo"]] = r["repo_name"]
    for r in repos:
        repo_name = r["repo_name"]
        merge_node(dry, "Repo", "name", repo_name,
                   {"remote": r["remote"], "path": r["main_repo"], "source": "git"})
        merge_rel(dry, "Repo", "name", repo_name, "RUNS_ON", "Host", "name", HOST_NAME)
        branch = r["branch"]
        if branch and branch != "HEAD":
            bkey = f"{repo_name}@{branch}"
            merge_node(dry, "Branch", "id", bkey, {"name": branch, "repo": repo_name, "source": "git"})
            merge_rel(dry, "Repo", "name", repo_name, "HAS_BRANCH", "Branch", "id", bkey)
        if r["is_worktree"]:
            # worktree 目录（可能已由 resreg 建过 -> MERGE 合并）
            merge_node(dry, "Worktree", "path", r["path"], {"source": "git"})
            merge_rel(dry, "Worktree", "path", r["path"], "BELONGS_TO", "Repo", "name", repo_name)
            if branch and branch != "HEAD":
                bkey = f"{repo_name}@{branch}"
                merge_rel(dry, "Worktree", "path", r["path"], "ON_BRANCH", "Branch", "id", bkey)

    # --- 容器 / 域名：应用部署 ---
    for c in containers:
        name = c["name"]
        merge_node(dry, "Container", "name", name,
                   {"image": c["image"], "vport": c["vport"], "source": "docker"})
        merge_rel(dry, "Container", "name", name, "RUNS_ON", "Host", "name", HOST_NAME)
        if c["vhost"]:
            merge_node(dry, "Domain", "name", c["vhost"], {"source": "docker"})
            merge_rel(dry, "Container", "name", name, "DEPLOYED_AT", "Domain", "name", c["vhost"])

    return {"claims": len(claims), "repos": len(repos), "containers": len(containers)}


def print_stats():
    data = cypher(
        f"MATCH (n:{MARKER}) WITH labels(n) AS ls "
        f"UNWIND ls AS l WITH l WHERE l <> '{MARKER}' "
        f"RETURN l AS label, count(*) AS c ORDER BY c DESC")
    total_n = cypher(f"MATCH (n:{MARKER}) RETURN count(n) AS c")["records"][0]["c"]
    total_r = cypher(f"MATCH (:{MARKER})-[r]->(:{MARKER}) RETURN count(r) AS c")["records"][0]["c"]
    print(f"\n=== GB10 数字孪生图统计 ===")
    print(f"节点: {total_n}   关系: {total_r}")
    print("按标签:")
    for rec in data["records"]:
        print(f"  {rec['label']}: {rec['c']}")


def main():
    ap = argparse.ArgumentParser(description="GB10 数字孪生知识图谱导入器")
    ap.add_argument("--dry-run", action="store_true", help="只打印将写入的节点/关系，不落库")
    ap.add_argument("--stats", action="store_true", help="导入后打印统计（默认即打印）")
    ap.add_argument("--no-wipe", action="store_true", help="不清空本子图（增量 MERGE）")
    args = ap.parse_args()

    if not args.dry_run and not args.no_wipe:
        print("清空旧 :GB10 子图 ...")
    wipe(args.dry_run) if not args.no_wipe else None

    counts = build(args.dry_run)
    print(f"采集: resreg claims={counts['claims']}, repos/worktrees={counts['repos']}, "
          f"containers={counts['containers']}")

    if not args.dry_run:
        print_stats()


if __name__ == "__main__":
    main()
