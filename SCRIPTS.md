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
