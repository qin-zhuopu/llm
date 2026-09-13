# 脚本索引（Scripts Registry）

> 本文件是所有 `scripts/*.py` 的单一登记处，配合 `scripts/check_scripts.py` 治理检查。
> 每个脚本必须：① 有模块级 docstring；② 支持 `-h`；③ 在本文件（或其他文档）登记。
> 详细的每个脚本用法见其 `-h` 输出。

## 数据流水线脚本（对应 AGENTS.md 7 阶段）

| 脚本 | 阶段 | 作用 | 状态 |
|------|------|------|------|
| `backfill_raw.py` | ② 保存原始资料 | 从 MD 提取来源 URL，回填原始资料到 `data/raw/`，含大小限制/secret 脱敏/`--force` 刷新 | ✅ 现役 |
| `build_kg.py` | ⑤ 知识图谱 | 从 YAML 构建 NetworkX 实体-关系图，输出 GraphML | ✅ 现役 |
| `check.py` | ⑥ 质量检查 | 三维度（业务/技术/来源）质量评分 | ✅ 现役 |
| `check_freshness.py` | ⑥ 质量检查 | 基于 sources.json 的 fetched_at 检查数据新鲜度 | ✅ 现役 |
| `validate.py` | ⑦ 测试 | 校验所有模型 YAML 符合 schema | ✅ 现役 |
| `validate_platforms.py` | ⑦ 测试 | 校验所有平台 YAML 符合 schema | ✅ 现役 |
| `test_all.py` | ⑦ 测试 | 集成测试（17 项） | ✅ 现役 |

## benchmark 来源标注脚本

| 脚本 | 作用 | 状态 |
|------|------|------|
| `suggest_benchmark_source.py` | 只读扫描并建议 benchmark 的 source 标注 | ✅ 现役 |
| `apply_benchmark_source.py` | 按规则批量应用 benchmark source 标注 | ✅ 现役 |

## 治理脚本

| 脚本 | 作用 | 状态 |
|------|------|------|
| `check_scripts.py` | 脚本治理检查（docstring / `-h` / 文档引用），纳入 test_all.py | ✅ 现役 |

## GB10 服务器数字孪生知识图谱（基础设施图，独立于模型数据图）

> 把本开发主机（GB10）的资源与业务实体建成可持续查询的 Neo4j 知识图谱。
> 与 `build_kg.py`（模型数据的 NetworkX 图）互不干扰：本图存于 Neo4j，节点统一挂 `:GB10` 标记标签。
> 数据源：resreg 注册表 `~/.jereh-cli/resource-registry.json` + git 仓库/worktree 拓扑 + docker 容器/域名。
> 依赖 `jc neo4j`（HTTP Query API），连接凭据存于 `jc env`（`NEO4J_BASE_URL/_USERNAME/_PASSWORD`），**凭据绝不入图/入库**。

| 脚本 | 作用 | 状态 |
|------|------|------|
| `import_resreg.py` | 采集本机资源/业务实体（resreg + git + docker），全量刷新 Neo4j `:GB10` 子图（幂等，支持 `--dry-run`/`--no-wipe`） | ✅ 现役 |
| `kg_query.sh` | 查询封装：`ports` / `owners` / `worktrees` / `apps` / `chrome` / `blast-radius <名称>` / `stats` / `cypher '<语句>'`，输出对齐表格 | ✅ 现役 |
| `_kg_render.py` | `kg_query.sh` 的表格渲染辅助（读 stdin 的 jc neo4j JSON，渲染 CJK 对齐表格） | ✅ 现役 |

本体（节点标签）：`Host` / `TestLine`(测试线) / `Port` / `Worktree` / `Directory` / `ChromeInstance` / `Repo` / `Branch` / `Container` / `Domain`。
关系：`OCCUPIES`(线→端口/目录) / `OWNS`(线→worktree) / `BELONGS_TO`(worktree→仓库) / `ON_BRANCH`(worktree→分支) / `HAS_BRANCH`(仓库→分支) / `LISTENS_ON`(实例→端口) / `SERVES`(实例→测试线) / `USES_PROFILE`(实例→目录) / `DEPLOYED_AT`(容器→域名) / `RUNS_ON`(→本机)。

维护（数据变了怎么刷新）：任何端口/worktree/容器/分支变动后，重跑 `python3 scripts/import_resreg.py` 即全量重建 `:GB10` 子图（先 DETACH DELETE 旧子图再重建，幂等）。

## 遗留脚本（Legacy，保留供参考，不推荐新用途）

| 脚本 | 作用 | 状态 | 替代方案 |
|------|------|------|---------|
| `extract_yaml.py` | 早期用 LLM API 从 MD 提取 YAML | ⚠️ 遗留 | 阶段④已改为**当前会话 Agent 手工提取**（见 AGENTS.md），本脚本仅作批量草稿备用 |
| `fetch_descriptions.py` | 早期从官网抓取描述存为 MD | ⚠️ 遗留 | 已被 `backfill_raw.py`（阶段②）取代 |

---

## 治理规则（强制）

1. **每个脚本必须有模块级 docstring**，说明作用、用法、参数。
2. **每个脚本必须支持 `-h`/`--help`** 且正常退出（退出码 0）。
3. **每个脚本必须在本文件或其他文档中登记**，避免"孤儿脚本"。
4. 上述规则由 `scripts/check_scripts.py` 自动检查，并纳入 `test_all.py` 门禁。
5. 新增脚本后运行 `python scripts/check_scripts.py` 确认达标。
