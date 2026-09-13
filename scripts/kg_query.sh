#!/usr/bin/env bash
# GB10 数字孪生知识图谱查询封装（Neo4j via `jc neo4j`）。
#
# 用途: 对 import_resreg.py 建好的 :GB10 子图做可读查询。
# 依赖: jc neo4j（凭据见 jc env：NEO4J_BASE_URL/_USERNAME/_PASSWORD）。
#
# 用法:
#   scripts/kg_query.sh ports                 # 所有端口 + 占用测试线 + 用途 + 监听的 Chrome 实例
#   scripts/kg_query.sh owners                # 各测试线（owner）占用的全部资源
#   scripts/kg_query.sh worktrees             # worktree -> 仓库/分支归属
#   scripts/kg_query.sh apps                  # 应用容器 -> 部署域名
#   scripts/kg_query.sh chrome                # Chrome 实例 -> 端口/profile/服务测试线
#   scripts/kg_query.sh jenkins <关键词>      # 按名模糊搜 Jenkins job（含文件夹路径/结果/最近构建）
#   scripts/kg_query.sh blast-radius <名称>   # 影响半径：某资源/测试线/仓库牵连的所有实体
#   scripts/kg_query.sh stats                 # 图规模统计
#   scripts/kg_query.sh cypher '<语句>'       # 直接跑一条 Cypher（表格输出）
#
# 说明: 结果用 jc neo4j 的 JSON 输出经 python 转为可读表格；每条命令 <=60s。

set -euo pipefail

JCTIMEOUT=55

run() {
  # $1 = cypher ; $2 = optional params json
  local cy="$1"; shift || true
  local params="${1:-}"
  if [[ -n "$params" ]]; then
    timeout "$JCTIMEOUT" jc neo4j query --cypher "$cy" --params "$params"
  else
    timeout "$JCTIMEOUT" jc neo4j query --cypher "$cy"
  fi
}

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RENDER_PY="$HERE/_kg_render.py"

# 把 jc neo4j 的 JSON records 渲染成对齐表格（读 stdin 的 JSON）
render() {
  python3 "$RENDER_PY"
}

cmd="${1:-help}"; shift || true

case "$cmd" in
  ports)
    run 'MATCH (p:Port:GB10)
         OPTIONAL MATCH (t:TestLine)-[:OCCUPIES]->(p)
         OPTIONAL MATCH (ci:ChromeInstance)-[:LISTENS_ON]->(p)
         RETURN p.value AS 端口, coalesce(t.name,"-") AS 占用测试线,
                coalesce(p.purpose,"-") AS 用途, coalesce(ci.name,"-") AS Chrome实例
         ORDER BY 端口' | render
    ;;
  owners)
    run 'MATCH (t:TestLine:GB10)
         OPTIONAL MATCH (t)-[r:OCCUPIES|OWNS]->(res)
         RETURN t.name AS 测试线, type(r) AS 关系,
                head([l IN labels(res) WHERE l<>"GB10"]) AS 资源类型,
                coalesce(res.value, res.path, "-") AS 资源
         ORDER BY 测试线' | render
    ;;
  worktrees)
    run 'MATCH (w:Worktree:GB10)
         OPTIONAL MATCH (w)-[:BELONGS_TO]->(repo:Repo)
         OPTIONAL MATCH (w)-[:ON_BRANCH]->(b:Branch)
         OPTIONAL MATCH (t:TestLine)-[:OWNS]->(w)
         RETURN w.path AS worktree, coalesce(repo.name,"-") AS 仓库,
                coalesce(b.name,"-") AS 分支, coalesce(t.name,"-") AS 归属测试线
         ORDER BY 仓库' | render
    ;;
  apps)
    run 'MATCH (c:Container:GB10)
         OPTIONAL MATCH (c)-[:DEPLOYED_AT]->(d:Domain)
         RETURN c.name AS 容器, coalesce(d.name,"(无域名)") AS 域名,
                coalesce(c.image,"-") AS 镜像
         ORDER BY 容器' | render
    ;;
  chrome)
    run 'MATCH (ci:ChromeInstance:GB10)
         OPTIONAL MATCH (ci)-[:LISTENS_ON]->(p:Port)
         OPTIONAL MATCH (ci)-[:USES_PROFILE]->(d:Directory)
         OPTIONAL MATCH (ci)-[:SERVES]->(t:TestLine)
         RETURN ci.name AS 实例, coalesce(p.value,"-") AS CDP端口,
                coalesce(d.path,"-") AS profile, coalesce(t.name,"-") AS 服务测试线
         ORDER BY 实例' | render
    ;;
  jenkins)
    kw="${1:-}"
    if [[ -z "$kw" ]]; then echo "用法: kg_query.sh jenkins <关键词>（按 job 名/文件夹路径模糊搜）"; exit 1; fi
    # 按 fullName 或 name 模糊匹配 job，带出所属文件夹（无则显示 server）与最近构建信息。
    run 'MATCH (j:JenkinsJob:Jenkins)
         WHERE toLower(j.fullName) CONTAINS toLower($q)
            OR toLower(coalesce(j.name,"")) CONTAINS toLower($q)
         OPTIONAL MATCH (f:Folder)-[:HAS_JOB]->(j)
         OPTIONAL MATCH (s:JenkinsServer)-[:HAS_JOB]->(j)
         RETURN j.fullName AS job,
                coalesce(f.fullName, s.name, "-") AS 归属,
                coalesce(j.type,"-") AS 类型,
                coalesce(j.lastResult,"NEVER_BUILT") AS 最近结果,
                coalesce(toString(j.lastBuildNumber),"-") AS 构建号,
                coalesce(j.lastBuildTime,"-") AS 最近构建
         ORDER BY job' "{\"q\": \"$kw\"}" | render
    ;;
  blast-radius)
    name="${1:-}"
    if [[ -z "$name" ]]; then echo "用法: kg_query.sh blast-radius <名称/端口/路径片段>"; exit 1; fi
    # 找到匹配节点（名称/value/path 任一包含），展开 1-2 跳邻居。
    # 关键：路径不得穿过 Host 中枢（所有实体都 RUNS_ON GB10，穿 Host 会牵出全图，无意义）。
    # 因此排除中间节点为 :Host 的路径，只保留有业务含义的牵连。
    run 'MATCH (n:GB10)
         WHERE toLower(coalesce(n.name,"")) CONTAINS toLower($q)
            OR coalesce(n.value,"") CONTAINS $q
            OR toLower(coalesce(n.path,"")) CONTAINS toLower($q)
         MATCH path=(n)-[*1..2]-(m:GB10)
         WHERE none(x IN nodes(path)[1..-1] WHERE x:Host)
           AND m <> n
         WITH n, m, relationships(path) AS rels, length(path) AS hops
         RETURN DISTINCT head([l IN labels(n) WHERE l<>"GB10"]) AS 源类型,
                coalesce(n.name,n.value,n.path) AS 源,
                hops AS 跳数,
                [r IN rels | type(r)] AS 关系链,
                head([l IN labels(m) WHERE l<>"GB10"]) AS 牵连类型,
                coalesce(m.name,m.value,m.path) AS 牵连实体
         ORDER BY 源, 跳数' "{\"q\": \"$name\"}" | render
    ;;
  stats)
    run 'MATCH (n:GB10) WITH labels(n) AS ls UNWIND ls AS l
         WITH l WHERE l<>"GB10" RETURN l AS 标签, count(*) AS 数量 ORDER BY 数量 DESC' | render
    echo
    run 'MATCH (:GB10)-[r]->(:GB10) RETURN type(r) AS 关系, count(*) AS 数量 ORDER BY 数量 DESC' | render
    ;;
  cypher)
    q="${1:-}"
    if [[ -z "$q" ]]; then echo "用法: kg_query.sh cypher '<Cypher 语句>'"; exit 1; fi
    run "$q" | render
    ;;
  help|-h|--help)
    sed -n '2,18p' "$0" | sed 's/^# \{0,1\}//'
    ;;
  *)
    echo "未知命令: $cmd"; echo "运行 'kg_query.sh help' 查看用法"; exit 1
    ;;
esac
