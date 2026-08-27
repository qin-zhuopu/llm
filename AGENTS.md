# AGENTS.md — 垂直领域大模型数据收集方法论

> 本文档是本项目的**核心方法论**，指导 AI Agent（及人类维护者）如何端到端地收集、整理、结构化、入图、质检一个垂直领域大模型的数据。
>
> 全流程共 7 个阶段：**搜索 → 保存原始资料 → 整理成 MD → 结构化成 YAML → 进入知识图谱 → 数据质量检查与修复 → 单元测试**。

---

## 全流程总览

```
① 搜索垂类模型          → 发现候选公司/产品
        ↓
② 获取并保存原始资料     → data/raw/{slug}/ + sources.json  （可用脚本批量处理）
        ↓
③ 整理成 MD             → domains/{domain}/{slug}.md         （可用脚本统一处理）
        ↓
④ 结构化成 YAML         → domains/{domain}/{slug}.yaml       （★必须在当前会话手工处理★）
        ↓
⑤ 进入知识图谱          → scripts/build_kg.py
        ↓
⑥ 数据质量检查与修复     → scripts/check.py
        ↓
⑦ 单元/集成测试         → scripts/validate.py + scripts/test_all.py
```

**关键分工原则：**

| 阶段 | 执行方式 | 原因 |
|------|---------|------|
| ①搜索 | Agent（web_fetch/搜索） | 需要联网和判断 |
| ②保存原始资料 | **可用脚本批量处理** | 机械性下载+存档，适合脚本 |
| ③整理成 MD | **可用脚本统一处理** | HTML→MD 转换是确定性操作 |
| ④结构化成 YAML | **★必须在当前会话手工处理，禁止用子代理，禁止直接调用 LLM API★** | 需要跨字段推理、交叉验证、理解语义，当前会话的 Agent 能力最强 |
| ⑤进入知识图谱 | 脚本 | 从 YAML 确定性构图 |
| ⑥质量检查 | 脚本 + Agent 修复 | 脚本打分，Agent 补数据 |
| ⑦测试 | 脚本 | 自动化验证 |

---

## 阶段 ① — 搜索垂直领域大模型

### 目标
发现在特定垂直行业形成商业化的闭源/专用大模型或模型系统公司。

### 有效搜索渠道（按命中价值排序）

> **铁律：跟着钱和榜单走，不要跟着关键词和模型目录走。**
> 垂类 AI 公司大多不自称"大模型公司"，不在任何模型目录（HuggingFace/OpenRouter/Models.dev）里——
> 这类目录对垂类模型命中率为 0，早期在此浪费大量精力。

| 优先级 | 渠道 | 用途 | 备注 |
|--------|------|------|------|
| ⭐⭐⭐ | **风投年度 State-of-AI 报告** | 发现新公司 | Menlo Ventures、Bessemer、Sequoia、a16z、CB Insights——系统爬整篇，提取所有点名公司 |
| ⭐⭐⭐ | **融资新闻/数据库** | 发现新公司 | 大额融资=商业化验证。搜"{领域} AI raises Series X"；Crunchbase/PitchBook |
| ⭐⭐ | 公司/产品官网 | 一手资料 | 最可靠，Harvey/Bloomberg/Abridge 从官网入手 |
| ⭐⭐ | snowball 顺藤摸瓜 | 找竞品 | 从已知公司延伸到竞争对手/合作伙伴 |
| ⭐⭐ | arXiv 论文 | 技术细节 | 模型原生型公司（Isomorphic/FengWu/ChatLaw）有论文 |
| ⭐ | GitHub Awesome-Domain-LLM / FinGPT | 开源垂类 | 华佗GPT、XuanYuan 等中文开源模型 |
| ❌ | 模型 API 目录（HF/OpenRouter/Models.dev） | 通用模型 | 对垂类命中率 0，**不要用来找垂类模型** |

### 关键认知
- **垂直领域闭源模型几乎不公开卖 API**（模型价值在排他性）。这个结论应触发"**转向产品官网+融资新闻+风投报告**"，而不是停止搜索。
- 真正的闭源垂类模型集中在大公司内部（Bloomberg、Harvey、蚂蚁百灵等）或产品型创业公司（不自称模型公司）。
- 区分三类公司：**模型原生型**（真正训练垂类基础模型，如 Isomorphic/Hippocratic）、**模型系统型**（自研专用模型+编排，如 Cognite/XBOW）、**工作流应用型**（主要调用通用模型+RAG/Agent，如 Harvey/Sierra）。三类都可收录，但要在 description/tags 中体现区别。
- 商业化信号（融资额、估值、ARR、客户数）是识别"垂类领先公司"的代理指标——优先追踪这些。

### 搜索方法论详见
`docs/search-methods.md`

---

## 阶段 ② — 获取并保存原始资料

### 目标
把搜索到的每一份原始内容**永久保存**，作为 MD 摘要的证据来源，可回溯、可审计。

### 目录结构（强制规范）

```
data/raw/{model-slug}/
├── sources.json            # 来源记录（必需）
├── official-website.md     # 官网抓取内容
├── arxiv-abstract.txt      # arXiv 论文
├── github-readme.md        # GitHub README
└── ...
```

- `{model-slug}` 与 `domains/` 下的文件名一致。
- **每一份原始资料都必须有对应的 URL**，记录在 `sources.json`。

### sources.json 格式

```json
{
  "files": [
    {
      "filename": "github-readme.md",
      "url": "https://github.com/PKU-YuanGroup/ChatLaw",
      "fetched_at": "2026-08-26",
      "type": "github"
    }
  ]
}
```

`type` 取值：`official-website`、`arxiv`、`github`、`blog`、`huggingface`、`paper-pdf`、`news` 等。

### 铁律
- **每次 web_fetch 获取到内容，必须同时保存到 `data/raw/{slug}/`**，不能只把摘要写进 MD 就丢掉原文。
- 原始资料是原始证据；MD 是整理后的二手摘要。任何 MD 中的数据都应能回溯到 raw 文件。

### 可脚本化
批量下载已知 URL 列表可用脚本处理（参考 `data/appliedcompute/download.py` 的模式：读 URL 列表 → 逐个抓取 → 存档）。详见 `data/raw/README.md`。

---

## 阶段 ③ — 整理成 MD（可用脚本统一处理）

### 目标
把原始资料（HTML/txt）整理成带 frontmatter 的结构化 MD 研究文档。

### MD 文件规范

- 路径：`domains/{domain}/{model-slug}.md`
- 头部 frontmatter：`title`、`date`、`source`（来源 URL）
- 正文：模型定位、技术细节、benchmark、商业数据、客户等
- **补充信息追加**：后续通过研究获取的新信息追加在文件末尾，用 `---` 分隔，标注来源 URL 和日期。不删除原有内容。

### 可脚本化处理
HTML → MD 是确定性转换，**可以用脚本统一处理**（参考 `data/appliedcompute/convert.py`：BeautifulSoup 提取正文 + html2text 转 MD + 生成 frontmatter）。

批量转换流程：
1. 从 `data/raw/{slug}/` 读取原始 HTML/内容
2. 提取正文、清理噪音
3. 生成带 frontmatter 的 MD
4. 写入 `domains/{domain}/{slug}.md`

---

## 阶段 ④ — 结构化成 YAML（★必须当前会话手工处理★）

### 目标
把 MD 研究文档结构化成符合 `schema/model.schema.json` 的 YAML 数据。

### ★★★ 强制规则 ★★★

> **本阶段必须在当前会话由当前 Agent 直接处理。**
> **禁止委派给子代理（sub-agent）。**
> **禁止直接调用 LLM API（如 extract_yaml.py 走 glm-4.5-air 那种模式）。**

### 为什么

历史教训（详见 `docs/extraction-strategy.md`）：

| 方式 | 技术字段均分 | 问题 |
|------|-------------|------|
| extract_yaml.py + glm-4.5-air + 8000字符截断 | 5/100 | 截断丢失 55% 内容；弱模型填充不足 |
| 当前会话 Agent 直接读 MD 提取 | 76-86/100 | 强模型 + 完整上下文 + 跨字段推理 |

- 当前会话的 Agent 本身就是强大模型，能力远超脚本调用的经济型模型。
- 直接读完整 MD（**禁止截断**），能交叉验证信息、推断缺失字段、保持字段间一致性。
- 不经过脚本中间层，没有截断、格式转换、token 限制等信息损失。

### 操作步骤（当前会话 Agent 执行）

1. 读 `schema/model.schema.json`，了解字段定义、枚举值、约束
2. 读 `domains/{domain}/{slug}.md` **完整内容**（禁止截断）
3. 参考高质量样例（如 `domains/legal/harvey-lab-agent.yaml`，得分 89）
4. 直接写 `domains/{domain}/{slug}.yaml`，尽量填全：
   - 必填：name, company, domain, status, description(≥30字符), capabilities(≥1项，建议≥4), references(≥1)
   - 技术字段尽量填：`parameters`、`architecture`、`base_model`、`training.stages`、`tech_stack`、`datasets`、`benchmarks`（含 comparison）
   - `domain` 必须与所在目录名一致，且是 schema 枚举之一
5. 若 MD 信息不足以填充技术字段 → 回到阶段①②补充研究，再回来提取

### 批处理建议
每批 10-15 个模型，每批结束跑 validate.py + test_all.py。

---

## 阶段 ⑤ — 进入知识图谱

### 目标
从 YAML 数据构建实体-关系知识图谱。

### 操作

```bash
python scripts/build_kg.py            # 构建并保存 GraphML + 输出统计
python scripts/build_kg.py --stats    # 只看统计
python scripts/build_kg.py --query "Bloomberg"  # 查询节点关系
```

### 图结构
- 节点类型：model、company、domain、base_model、tag、access_type、platform
- 关系：company→developed→model、model→in_domain→domain、model→based_on→base_model、model→tagged→tag、model→accessible_via→access_type
- 输出 `kg_data.graphml`，可用 Gephi/yEd/Cytoscape 可视化

### 说明
知识图谱从 YAML **动态构建**，不硬编码任何模型/域列表。新增 YAML 后重新运行即自动纳入。

---

## 阶段 ⑥ — 数据质量检查与修复

### 目标
量化每个模型 YAML 的数据质量，发现并修复短板。

### 三维度评分（scripts/check.py）

| 维度 | 缩写 | 评估内容 |
|------|------|----------|
| 业务 | B | description、capabilities、access、website、references |
| 技术 | T | parameters、architecture、base_model、training、tech_stack、datasets、benchmarks |
| 来源 | S | MD 内容长度、具体数据点、**data/raw/ 原始资料的来源数量与类型质量**（基于 sources.json） |

> **来源(S)维度说明**：自 2026-08 起，S 维度改为基于 `data/raw/{slug}/sources.json` 评分——
> 来源数量+多样性(0-25) + 来源类型质量(0-20，论文/repo > 官方 > 新闻)。
> 这比旧的"MD 正则匹配"更准确地反映真实来源证据。无 raw 时降级用 MD 回退。

### 数据新鲜度（scripts/check_freshness.py）

垂类 AI 公司融资/估值/benchmark/客户数变化快，原始资料需定期刷新。

```bash
python scripts/check_freshness.py            # 全量新鲜度报告
python scripts/check_freshness.py --stale     # 只列 stale + expired（需刷新）
python scripts/check_freshness.py --missing   # 缺 sources.json/fetched_at 的
```

新鲜度分级（基于 sources.json 的 fetched_at）：fresh(≤90天) / aging(≤180) / stale(≤365) / expired(>365)。

刷新过期数据：
```bash
python scripts/backfill_raw.py --slug {slug} --force   # 强制重抓
```

### 操作

```bash
python scripts/check.py                              # 全量评分 + 均分
python scripts/check.py --top 10                     # 最高分
python scripts/check.py --bottom 10                  # 最低分（优先修复）
python scripts/check.py --details domains/legal/harvey-lab-agent.yaml  # 单文件详情
python scripts/check.py --domain finance             # 按领域
```

### 修复流程
1. `check.py --bottom N` 找出低分模型
2. 判断根因：
   - **技术字段空** → 回阶段①②补充研究（官网/论文/GitHub），把技术细节追加到 MD，再回阶段④重新提取
   - **MD 信息不足** → 回阶段①②重新搜索更丰富来源
3. 修复后重新 `check.py --details` 确认提升

### 质量目标
- 综合均分目标 ≥ 70
- 单个模型技术维度尽量 ≥ 60（有基座模型、训练阶段、benchmark）

---

## 阶段 ⑦ — 单元/集成测试

### 目标
确保脚本正常、YAML 合规、数据一致。

### 操作

```bash
python scripts/validate.py             # schema 校验所有 domains/**/*.yaml
python scripts/validate_platforms.py   # 校验 platforms/*.yaml
python scripts/test_all.py             # 集成测试（17项）
```

### test_all.py 覆盖
- validate.py 全通过
- check.py 能跑 + --top/--bottom/--details 正常
- build_kg.py 图构建成功 + 节点数 > 100
- validate_platforms.py 通过
- Schema 一致性（脚本不引用已删除字段）
- 所有 YAML 字段都在 schema 中定义

### 铁律
- 每次新增/修改 YAML 后必须跑 `validate.py`
- 提交前必须跑 `test_all.py`，17 项全绿才提交
- 修改 schema（如新增 domain 枚举）后必须跑 `test_all.py` 确认无回归

---

## 方法论自检：现有流程的问题与优化方向

> 以下是对本方法论的批判性审视，供持续改进。

### 已发现并已修复的问题
1. ~~extract_yaml.py 8000 字符截断~~ → 已禁止截断（阶段④改为当前会话手工处理）
2. ~~原始资料只存摘要不存原文~~ → 已建立 `data/raw/` 强制保存机制（阶段②）
3. ~~用弱模型 glm-4.5-air 提取质量差~~ → 已改为当前会话 Agent 直接提取
4. ~~raw 资料未全量回填~~ → 已用 `scripts/backfill_raw.py` 回填全部 100 个模型
5. ~~README 知识图谱描述与实现不符（宣称 LightRAG + query_kg.py，实际是 NetworkX）~~ → 已修正 README，如实描述 NetworkX 实现
6. ~~benchmark 数据未区分公司自报 vs 第三方~~ → 已在 schema 增加 `benchmarks[].source` 字段，并标注关键模型

### benchmark 数据来源标注（source 字段）

schema 的 `benchmarks[].source` 用于标注每条评测数据的可信度口径：

| 值 | 含义 |
|----|------|
| `self-reported` | 公司自报，未经审计（如自招护士评估、ARR、客户案例） |
| `third-party` | 第三方独立评测/验证（如独立实验室合成验证） |
| `paper` | 学术论文/同行评审（如 arXiv、Nature） |
| `leaderboard` | 公开排行榜（如 HackerOne、MatBench） |
| `unknown` | 无法确定（需人工判断） |

**标注方法**：`scripts/suggest_benchmark_source.py` 只读扫描并给出启发式建议，但**实际标注必须由当前会话 Agent 结合 raw 资料人工确认**（不可脚本盲改，因为启发式对 ~90% 的 comparison 文本无法可靠判断）。新增模型时应在阶段④同步填写 source。

### 仍存在的问题与优化建议

**所有自检问题均已解决：**

| # | 问题 | 解决方式 |
|---|------|---------|
| 1 | 来源维度(S)分数偏低 | ✅ 全部 100 模型回填 2-3 个独立来源；S 维度改为基于 sources.json 评分 |
| 2 | benchmark source 未标注 | ✅ 全部 312 条已标注（apply_benchmark_source.py 规则应用 + 关键模型人工确认） |
| 3 | raw 资料未全量回填 | ✅ backfill_raw.py 回填全部 100 模型 |
| 4 | 阶段③脚本化未落地 | ✅ backfill_raw.py（阶段②）+ appliedcompute 的 download/convert 模式可复用 |
| 5 | 知识图谱静态快照 | ⚪ 保留（当前 100 模型全量重建耗时可忽略，数据量大时再优化增量更新） |
| 6 | 缺数据新鲜度跟踪 | ✅ check_freshness.py + backfill_raw.py --force；全部 100 模型 fresh |
| 7 | domain 分类边界模糊 | ✅ README 说明"垂类工作流应用"收录原则；software-development/customer-service 入 schema |
| 8 | check.py 来源评分依赖 MD 正则 | ✅ 改为基于 data/raw/sources.json 的来源数量+类型质量评分 |
| 新 | README 知识图谱描述失实(LightRAG) | ✅ 修正为如实描述 NetworkX 实现 |

### 流程健壮性建议
- **幂等性**：所有阶段应可重复执行而不产生副作用（当前基本满足）
- **可回溯**：raw → MD → YAML 的链路应始终可追溯（sources.json 是关键）
- **分批 + 验证**：每批处理后立即验证，避免批量错误累积
- **提交粒度**：按逻辑批次提交，commit message 说明数据来源和处理方式

---

## 快速参考：新增一个垂类模型的最小步骤

```bash
# ① 搜索（Agent 联网研究，确定公司和 domain）

# ② 保存原始资料
#    web_fetch 官网/论文 → 写入 data/raw/{slug}/official-website.md 等
#    创建 data/raw/{slug}/sources.json（每个文件带 URL）

# ③ 整理 MD（可脚本化）
#    → domains/{domain}/{slug}.md（带 frontmatter + 来源）

# ④ 结构化 YAML（★当前会话手工，禁止子代理/禁止直接调 LLM API★）
#    读 schema + 读完整 MD → 写 domains/{domain}/{slug}.yaml

# ⑤ 入图
python scripts/build_kg.py

# ⑥ 质检
python scripts/check.py --details domains/{domain}/{slug}.yaml

# ⑦ 测试
python scripts/validate.py && python scripts/test_all.py

# 提交
git add -A && git commit -m "feat: add {model} data with raw materials"
```

---

## 相关文档
- `docs/search-methods.md` — 搜索垂类模型的详细渠道和技巧
- `docs/extraction-strategy.md` — 提取策略的演进和经验教训
- `data/raw/README.md` — 原始资料目录规范
- `schema/model.schema.json` — 模型 YAML 的字段定义
- `CHANGELOG.md` — schema 和数据的变更历史
