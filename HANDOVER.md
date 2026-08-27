# 项目交接文档（HANDOVER）

> 面向后续接手者（人或 AI Agent）的项目现状快照与工作指南。
> 更新日期：2026-08-26 · 对应 commit：`5b91bc3`

---

## 1. 项目是什么

**商业垂直领域大模型（垂类 AI）数据集与市场报告项目。**

收集在特定行业形成商业化的垂类 AI 模型/产品，结构化为 YAML 数据，构建知识图谱，做数据质量评分，并产出市场分析报告。

- 数据是"垂类 AI 公司/产品"，不是通用大模型
- 每条数据可回溯到原始抓取资料（`data/raw/`）
- 核心方法论见 **`AGENTS.md`**（7 阶段流水线）

---

## 2. 当前状态快照

| 指标 | 数值 |
|------|------|
| 模型总数 | **198**（跨 22 个领域） |
| 平台数 | 3（Tinker、Applied Compute、John Snow Labs） |
| raw 资料覆盖 | 198/198（100%） |
| benchmark 总数 | 561（100% 标注 source） |
| 脚本 | 12 个（全部有 docstring + 支持 -h + 已登记） |
| 文档 | AGENTS/README/SCRIPTS/CHANGELOG + docs/ 下 5 篇 |
| 综合质量分 | 75（业务 93 / 技术 73 / 来源 59），排除 data-scarce 后 76 |
| ≥70 分（报告可用） | ~136 个 |
| 集成测试 | 18/18 通过 |
| 最新分支 | main（已与 origin 同步） |

> 注：schema 新增了可选 `data_quality` 字段，区分低来源模型是 `coverage-gap`（P1 待补）还是 `data-scarce`（客观信息稀缺，补不到）。当前 9 个标为 data-scarce。check.py 会分别统计。

---

## 3. 目录结构

```
domains/{领域}/{slug}.yaml   # 模型结构化数据（198个）
domains/{领域}/{slug}.md     # 模型研究文档（MD 摘要）
data/raw/{slug}/             # 每个模型的原始抓取资料 + sources.json
platforms/                   # AI 平台数据 + schema
schema/model.schema.json     # 模型 YAML 的 JSON Schema（含 business/benchmarks.source 字段）
scripts/                     # 12 个工具脚本（见 SCRIPTS.md）
docs/                        # 报告、提纲、复盘、方法论文档
AGENTS.md                    # ★核心方法论（必读）
SCRIPTS.md                   # 脚本索引
README.md / CHANGELOG.md     # 项目说明 / 变更历史
```

---

## 4. 关键文档导航

| 文档 | 用途 | 何时读 |
|------|------|--------|
| `AGENTS.md` | **7 阶段数据收集方法论 + 铁律** | 新增/修改数据前必读 |
| `SCRIPTS.md` | 12 个脚本的索引和状态 | 想知道用哪个脚本 |
| `docs/search-methods.md` | 搜索垂类模型的渠道（跟着钱和榜单走） | 阶段① 搜索时 |
| `docs/extraction-strategy.md` | 提取策略演进和教训 | 理解为何禁用弱模型/截断 |
| `docs/report-outline.md` | 报告提纲（为什么写/数据缺陷/迭代方向） | 写报告前 |
| `docs/vertical-llm-market-report.md` | 市场报告成品（v3，198 模型） | 看结论 |
| `docs/data-quality-review.md` | 数据质量复盘 | 了解数据短板 |
| `data/raw/README.md` | 原始资料目录规范 | 保存 raw 时 |

---

## 5. 已完成的工作（时间倒序）

1. **合并 feat/deep-search-3-domains** → 模型 110 → 198（+88：零售/HR/制造/物流/汽车/材料/农业/客服等）
2. **报告 v3 + 数据复盘更新** → 反映 198 模型的新格局（多领域开花）
3. **脚本治理（方案 B）** → check_scripts.py + SCRIPTS.md，强制 docstring/-h/文档登记，纳入 test_all
4. **知识图谱扩展（方案 A）** → build_kg.py 增加 script/doc 节点和 doc→documents→script 关系
5. **数据质量复盘 + 字段修复** → 关键字段 0 缺失
6. **两轮新渠道搜索** → 发现 10 家报告未覆盖的公司（Hebbia/EvenUp/Norm Ai/Eudia/Decagon/Abnormal/Material Security/Tomorrow.io/Paradox/Eilla）
7. **benchmark source 全量标注** → 561 条全部标注可信度来源
8. **raw 资料全量回填** → 198 模型全部有原始资料 + sources.json
9. **schema 演进** → 新增 software-development/customer-service 域、benchmarks.source 字段、business 字段
10. **方法论沉淀** → AGENTS.md 完整 7 阶段 + 自检

---

## 6. 待办事项（按优先级）

> 详见 `docs/report-outline.md` 第五节 P1-P5。

| 优先级 | 任务 | 说明 | 状态 |
|--------|------|------|------|
| **P1** | 提升来源多样性 | **122/198（62%）模型仅单一来源**，拉低来源维度(57)。补抓论文/新闻/第三方来源，目标每模型 ≥2 来源。用 `backfill_raw.py`（需联网搜新 URL） | 🔴 最大短板 |
| **P2** | 补充结构化商业字段 | schema 已加 `business` 字段（funding/valuation/arr/customers/investors），已填 Isomorphic 1 个，**其余 197 个待填**（当前会话手工，数据在 MD/raw 里） | 🟡 进行中 |
| **P3** | 平衡领域覆盖 | 政务/软件开发仅 1 个，可针对性补充 | 🟡 |
| **P4** | 扩大样本减偏差 | 系统爬风投报告（Menlo/Bessemer/a16z），减少幸存者偏差 | 🟢 |
| **P5** | 数据新鲜度维护 | 定期 `check_freshness.py --stale` + `backfill_raw.py --force` 刷新 | 🟢 |
| — | 新增 88 模型质量复核 | 合并进来的模型质量分未逐个人工复核，部分来源分偏低 | 🟡 |

---

## 7. 铁律（必须遵守）

来自 `AGENTS.md`，违反会导致数据质量倒退：

1. **阶段④ YAML 结构化必须当前会话手工做** —— 禁止委派子代理，禁止调用 glm-4.5-air 等弱模型 API（历史教训：弱模型技术分只有 5/100，当前会话直接做 76-86/100）。
2. **禁止截断 MD** —— 读完整内容再提取。
3. **每次 web_fetch 必须保存原始资料到 `data/raw/{slug}/`** + sources.json（每份资料带 URL）。
4. **提交前必须跑 `python scripts/test_all.py`，18 项全绿才提交。**
5. **每个新脚本必须有 docstring + 支持 -h + 在 SCRIPTS.md 登记**（`check_scripts.py` 会检查）。
6. **benchmark 尽量标注 `source`**（self-reported/paper/third-party/leaderboard）。

---

## 8. 常用命令

```bash
# 环境（依赖偶尔会丢，重装即可）
pip install -r requirements.txt

# 验证 + 测试（提交前必跑）
python scripts/validate.py          # schema 校验
python scripts/test_all.py          # 18 项集成测试

# 质量检查
python scripts/check.py             # 全量三维度评分
python scripts/check.py --bottom 15 # 最低分（优先修复）
python scripts/check.py --details domains/legal/chatlaw.yaml

# 数据新鲜度 / 治理 / 图谱
python scripts/check_freshness.py --stale
python scripts/check_scripts.py
python scripts/build_kg.py --stats

# 回填原始资料
python scripts/backfill_raw.py --slug {slug}          # 补单个
python scripts/backfill_raw.py --slug {slug} --force  # 刷新
```

---

## 9. 环境与限制注意事项

- **依赖偶尔丢失**：沙盒环境重置后 `yaml` 等模块会没，跑脚本前先 `pip install -r requirements.txt`。
- **GitHub 网关限制**：`gh api PATCH /repos/...`（改仓库设置/可见性）返回 403，无法通过工具改。需手动在 GitHub 网页操作。
- **推送保护**：抓取的第三方网页可能含 secret（Mapbox token 等）触发 push protection；`backfill_raw.py` 已加 secret 脱敏和 500KB 大小上限。
- **大文件**：抓取可能带入超大媒体文件，`backfill_raw.py` 已限制，但合并旧分支时需检查 `find data/raw -type f -size +1M`。

---

## 10. 分支状态

- **main**：当前工作分支，与 origin 同步。
- 远程还有 24 个历史开发分支（feat/*、docs/* 等），**均落后 main 28-53 个提交，是已被 main 取代的旧实现，不要合并**（会引入倒退，如恢复已删除的 LightRAG/quality_check 代码）。唯一有价值的 `feat/deep-search-3-domains` 已于 `45e8726` 合并。
