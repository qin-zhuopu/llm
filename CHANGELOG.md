# 变更日志

## Schema 变更：新增可选字段 `data_quality`

#### 新增 `data_quality` 字段（可选，object，additionalProperties: false）
用于标注「条目质量低」的根因，区分**可补** vs **补不到**。含三个可选子字段：
- `completeness`：`full` / `partial` / `minimal`——信息完整度自评。
- `gap_reason`：`coverage-gap`（有公开资料但搜索/抓取不足，理论上可补）/ `data-scarce`（公司闭源、无公开资料，客观稀缺补不到）/ `not-applicable`（已充分无缺口）。
- `note`：简要说明缺口原因的字符串。

字段不加入 `required`，对现有 198 个条目零影响；因 schema `additionalProperties: false`，已显式定义以允许带此字段的 YAML 通过校验。

#### `check.py` 保守增强（不改动三维度打分算法）
- 全量汇总额外打印 data-scarce 条目数与「排除 data-scarce 后的综合均分」。
- `--details` 输出附带 `data_quality.gap_reason` 标注。
- 新增可选开关 `--exclude-scarce`，在展示列表中剔除 data-scarce 条目。
- 现有评分对照不变（综合均分 74 / B92 / T73 / S57），`test_all.py` 17 项仍全绿。

#### 文档
- `AGENTS.md` 阶段⑥新增 `data_quality` 字段用途、三个 `gap_reason` 含义及填写规范。

---

## 2026-08-26 (数据质量复盘)

### 复盘与修复
- 新增 `docs/data-quality-review.md`：全量数据质量复盘报告
- 修复关键字段缺失：ant-bailing 补全 training/datasets/benchmarks（技术分 25→71）、wayve-lingo 和 microsoft-mattergen 补全 benchmarks
- 修复后：缺 benchmarks/training/datasets 的模型均为 0
- 现状：110 模型 + 3 平台，综合质量分 78（B:95/T:77/S:64），343 条 benchmark 全标注 source，100% 有 raw 资料且 fresh

### 两轮新渠道搜索成果（累计 +10 家报告未覆盖公司）
- 第一轮：Hebbia、EvenUp、Norm Ai、Eudia、Decagon
- 第二轮：Abnormal AI、Material Security、Tomorrow.io、Paradox、Eilla

---

## 2026-08-26

### Schema v3 变更

#### 新增 2 个 domain 枚举值
- `software-development`（软件开发，如 Cursor）
- `customer-service`（客户服务，如 Sierra）
- 相应更新 README 领域分类和收录原则（垂类工作流应用作为例外收录）

#### 新增 `benchmarks[].source` 字段（可选）
标注每条评测数据的可信度口径：`self-reported` / `third-party` / `paper` / `leaderboard` / `unknown`。
用于区分公司自报数据 vs 第三方验证 vs 论文，提升数据可信度透明度。

### 数据与工具
- 新增 `scripts/backfill_raw.py`：从 MD 提取来源 URL 回填原始资料到 `data/raw/`，含内容类型过滤、500KB 大小上限、`--force` 刷新
- 全部 100 个模型完成 raw 资料回填（每个含 sources.json）
- 新增 `scripts/suggest_benchmark_source.py`：扫描并建议 benchmark source 标注（只读）
- 新增 `scripts/apply_benchmark_source.py`：按规则批量应用 benchmark source 标注
- 新增 `scripts/check_freshness.py`：基于 sources.json 的 fetched_at 检查数据新鲜度
- **全部 312 条 benchmark 完成 source 标注**（self-reported/third-party/paper/leaderboard）
- **check.py 来源(S)维度改为基于 data/raw/sources.json 评分**（来源数量+类型质量），替代旧的 MD 正则
- 全部 100 模型 sources.json 齐全且新鲜度为 fresh
- 修正 README 知识图谱章节：如实描述 NetworkX 实现（此前错误宣称 LightRAG + 不存在的 query_kg.py）
- 新增 `AGENTS.md`：完整 7 阶段数据收集方法论，含全部自检问题的解决记录

---

## 2026-08-25

### Schema v2 重大变更

#### `access` 字段从单选改为多选数组

**变更内容：** `access` 字段类型从 `string` 改为 `array`

**原因：** 一个模型可以同时有多种获取方式（如 DeepSeek 既开放权重又提供 API）

**影响范围：**

| 文件 | 影响 |
|------|------|
| `schema/model.schema.json` | `access` 类型从 `string` → `array`，items 保持原 enum |
| `schema/example.yaml` | `access: internal-only` → `access: [internal-only]` |
| `domains/**/*.yaml` (65 个) | 全部已自动迁移为单元素数组 |
| `scripts/extract_yaml.py` | **无需修改** — prompt 从 schema 动态生成，自动适配新类型 |
| `scripts/validate.py` | **无需修改** — 基于 jsonschema 验证，跟随 schema 变化 |
| `scripts/quality_check.py` | **无需修改** — 未对 access 做类型检查 |
| `scripts/restore_metadata.py` | **注意** — 恢复 access 字段时需确保写入数组格式 |

**迁移示例：**

```yaml
# 之前
access: api

# 之后
access:
  - api

# 多选示例
access:
  - open-weights
  - api
```

**枚举值（不变）：** `api`, `saas`, `private-deployment`, `open-weights`, `internal-only`, `unknown`

---

#### 删除 HuggingFace 形式字段，新增训练/技术/评测字段

**删除：** `language`, `license`, `license_name`, `license_link`, `pipeline_tag`, `co2_eq_emissions`, `model_index`

**新增：**

| 字段 | 说明 |
|------|------|
| `architecture` | 模型架构 |
| `training.stages[]` | 训练阶段（pre-training/sft/rlhf/dpo 等） |
| `training.total_tokens` | 总训练量 |
| `training.total_cost` | 训练成本 |
| `training.context_length` | 上下文窗口 |
| `tech_stack.framework` | 训练框架 |
| `tech_stack.inference` | 推理引擎 |
| `tech_stack.techniques[]` | 关键技术 |
| `datasets[]` | 训练数据集 |
| `benchmarks[]` | 评测结果 |
| `api` | API 接入信息 |

**影响范围：** 新增字段全部 optional，不影响现有 YAML 文件。

---

#### `description` 最小长度从 10 提高到 30

**影响：** 新增模型的 description 必须 ≥ 30 字符。已有文件已在数据质量修复中全部满足。

---

### 新增 platforms/ 目录

新增 AI 平台收录体系，与 `domains/` 并列。

- `platforms/schema.json` — 平台 schema（`inference_api` 为必填）
- `platforms/tinker.yaml` — 首个录入的平台（Thinking Machines Lab）
- `scripts/validate_platforms.py` — 平台文件验证脚本
