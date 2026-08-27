# 数据质量复盘报告

> 日期：2026-08-26（合并 feat/deep-search-3-domains 后更新）
> 范围：全部 **198** 个模型 + 3 个平台（较上版 110 个新增 88 个）
> 工具：scripts/check.py（三维度评分）、validate.py、test_all.py、check_freshness.py

## 0. 合并更新说明（198 模型）

合并 `feat/deep-search-3-domains` 分支后，模型从 110 → 198（+88），覆盖领域更均衡。
关键指标变化：

| 指标 | 合并前(110) | 合并后(198) | 说明 |
|------|:---:|:---:|------|
| 综合均分 | 78 | **74** | 新增模型多为单来源，拉低来源维度 |
| 业务(B) | 95 | 92 | 基本持平 |
| 技术(T) | 77 | 73 | 略降 |
| 来源(S) | 64 | **57** | 主要短板：单来源模型从 53 → 122 |
| benchmark 总数 | 343 | 561 | 全部标注 source |
| ≥70 分(可入报告) | 90 | **136** | 62 个 <70 |

**核心问题（P1 待办放大）**：122/198（62%）模型仅单一来源，是来源维度下滑的直接原因。新增模型业务信息完整（B 均 92）但缺多来源交叉验证。

---

## 1. 数据规模总览

| 指标 | 数值 |
|------|------|
| 模型总数 | 110 |
| 平台数 | 3（Tinker、Applied Compute、John Snow Labs 候选） |
| 覆盖领域 | 22 个 |
| raw 资料覆盖 | 110/110（100%） |
| benchmark 总数 | 343 条（100% 标注 source） |
| 数据新鲜度 | 100% fresh |

### 领域分布

| 梯队 | 领域（模型数） |
|------|--------------|
| 密集（≥8） | finance(14)、materials-science(10)、legal(10)、healthcare(10)、pharma-biotech(8) |
| 中等（4-6） | retail-ecommerce(6)、aerospace-defense(6)、media-entertainment(5)、agriculture(5)、human-resources(4)、education(4)、automotive(4) |
| 稀疏（1-3） | telecom(3)、manufacturing(3)、logistics-supplychain(3)、energy(3)、construction-realestate(3)、climate-environment(3)、customer-service(2)、accounting-audit(2)、software-development(1)、government(1) |

---

## 2. 三维度质量评分

**综合平均 78 / 100**（业务 95 · 技术 77 · 来源 64）

| 维度 | 均分 | 评价 |
|------|------|------|
| 业务 (B) | 95 | 优秀。description/capabilities/references/website 基本完备 |
| 技术 (T) | 77 | 良好。绝大多数有 training/benchmarks/tech_stack；本轮修复后无缺失 |
| 来源 (S) | 64 | 有提升空间。53 个模型仅 1 个来源，是拉低 S 的主因 |

### 分数梯队
- Top 模型（85-93）：GNoME、华佗GPT、BloombergGPT、AC GLM-5.1、网易伏羲、GraphCast 等（有论文 + 多来源）
- 底部模型（59-69）：多为来源单一（仅官网 1 个来源），技术数据齐全但缺论文/多来源交叉验证

---

## 3. 本轮发现并修复的问题

| 问题 | 影响范围 | 修复 |
|------|---------|------|
| 缺 benchmarks | 3 个（ant-bailing、wayve-lingo、microsoft-mattergen） | ✅ 从 MD 提取补全 |
| 缺 training | 1 个（ant-bailing） | ✅ 补全 pre-training/post-training |
| 缺 datasets | 1 个（ant-bailing） | ✅ 补全金融语料 + SkySense |
| 蚂蚁百灵技术分低（25） | 单模型 | ✅ 补全后 25→71，综合 59→74 |

修复后：**缺 benchmarks/training/datasets 的模型均为 0**。

### 数据结构健康度（修复后）
- 无缺 website、无 description < 50 字符、无单来源缺失
- 全部 110 模型通过 schema 校验
- 17 项集成测试全绿

---

## 4. benchmark 数据可信度分布

| source | 条数 | 占比 |
|--------|------|------|
| self-reported（公司自报） | 314 | 91.5% |
| paper（论文/同行评审） | 17 | 5.0% |
| leaderboard（公开排行榜） | 8 | 2.3% |
| third-party（第三方验证） | 4 | 1.2% |

**关键洞察**：91.5% 的 benchmark 是公司自报口径——这印证了市场报告的核心结论：**垂类 AI 领域几乎没有公司的性能数据经过独立第三方验证**。使用本数据集时应清醒认识到，绝大多数性能声明来自厂商自身，不等于真实业务结果。

---

## 5. 来源多样性分布

| 来源数量 | 模型数 | 占比 |
|---------|--------|------|
| 3+ 个来源 | 34 | 31% |
| 2 个来源 | 23 | 21% |
| 1 个来源 | 53 | 48% |

近半数模型仅有单一来源（多为官网），这是来源维度(S)偏低的直接原因。

---

## 6. 待改进项（低优先级，持续任务）

| # | 问题 | 建议 |
|---|------|------|
| 1 | 48% 模型仅单一来源 | 对高价值模型补抓论文/新闻/第三方来源，提升交叉验证 |
| 2 | 领域分布不均 | government/software-development 仅 1 个；可针对性扩充 |
| 3 | 91.5% benchmark 为自报 | 属行业客观现状，无法根本改变；已通过 source 字段透明标注 |
| 4 | 知识图谱静态重建 | 当前 110 模型全量重建耗时可忽略，数据量大时再优化增量 |

---

## 7. 结论

数据集整体质量健康（综合 78/100），结构完整性问题已全部修复（关键字段 0 缺失）。核心优势：
- **可回溯**：110 模型全部有 raw 原始资料 + sources.json
- **透明**：343 条 benchmark 全部标注可信度来源
- **一致**：全部通过 schema 校验和集成测试

主要提升空间在**来源多样性**（近半数单一来源）——这是持续性工作，不影响数据的结构完整性和可用性。
