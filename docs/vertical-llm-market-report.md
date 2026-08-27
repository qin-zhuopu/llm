# 商业垂直领域大模型市场报告（基于本数据集）

> 数据来源：本仓库 `domains/` 结构化数据集
> 覆盖：110 个垂类模型/产品，跨 22 个领域，3 个 AI 平台
> 质量门槛：仅纳入综合质量分 ≥ 70 的 90 个模型（排除 20 个低质量数据）
> 编制日期：2026-08-26
> 数据可信度声明：本报告性能数据 91.5% 为公司自报口径（见第 5 节），不等于经审计的真实业务结果

---

## 执行摘要

基于本数据集 90 个高质量垂类模型的结构化分析，得出三个核心判断：

**1. 垂类 AI 的商业化高度集中在少数"高价值 + 强闭环"领域**
金融、法律、医疗、材料科学、药物研发五个领域贡献了本数据集近半数（45/90）的高质量模型，且平均质量分最高。这些领域的共同点是：数据专有性强、结果可验证、错误代价高。

**2. 性能数据的可信度是行业系统性短板**
本数据集 343 条 benchmark 中，**91.5% 为公司自报**，仅 5% 有论文支撑、1.2% 经第三方验证。这与市场共识一致——垂类 AI 的"性能领先"绝大多数未经独立验证。

**3. 三类公司形态并存，模型不再是唯一护城河**
模型原生型（Isomorphic、华佗GPT、BloombergGPT）、模型系统型（Cognite、XBOW、Abnormal）、工作流应用型（Harvey、Sierra、Hebbia）三类并存。商业化领先 ≠ 模型领先，真正的壁垒是"模型 + 专有数据 + 工作流 + 结果反馈"的闭环。

---

## 1. 领域分布与成熟度

按高质量模型密度和最高分排序：

| 梯队 | 领域 | 高质量模型数 | 代表（综合分） |
|------|------|:---:|------|
| **Tier 1** | 金融 | 10 | 度小满轩辕(96)、AlphaSense(86)、BloombergGPT(83) |
| **Tier 1** | 法律 | 9 | ChatLaw(93)、CoCounsel(91)、Harvey Review Table(91) |
| **Tier 1** | 医疗 | 10 | 华佗GPT(91)、Abridge(88)、Nabla(85) |
| **Tier 1** | 药物研发 | 8 | Isomorphic IsoDDE(87)、Recursion(82)、Deep Origin(82) |
| **Tier 1** | 材料科学 | 8 | GNoME(93)、Chemify(79)、Atinary(79) |
| **Tier 2** | 零售电商 | 5 | Shopify Sidekick(86)、Amazon Rufus(82)、DoorDash(81) |
| **Tier 2** | 媒体娱乐 | 4 | 网易伏羲(85)、Jasper(85)、阅文妙笔(83) |
| **Tier 2** | 人力资源 | 4 | LinkedIn Hiring(89)、Eightfold(78)、Paradox |
| **Tier 2** | 制造业 | 3 | 腾讯混元工业版(90)、Siemens Copilot(85) |
| **Tier 2** | 汽车 | 3 | Cerence CaLLM(89)、理想Mind GPT(84) |
| **Tier 2** | 物流供应链 | 3 | FourKites(89)、顺丰科技(85) |
| **Tier 2** | 教育 | 3 | 有道子曰(84)、学而思MathGPT(81) |
| **Tier 2** | 航空航天/国防 | 3 | Scale Donovan(81)、Shield Hivemind(80)、XBOW(75) |
| **Tier 3** | 会计审计/气象/电信/农业/建筑/客服/政务/软件开发/能源 | 1-2 | CoCounsel Tax(90)、GraphCast(87)、九天(86)、通义政务(87) |

**观察**：Tier 1 五大领域不仅模型密集，且最高分普遍 ≥87，说明这些领域的数据积累和技术成熟度最高。

---

## 2. 三类公司形态分析

| 类型 | 定义 | 本数据集代表 | 护城河 |
|------|------|------------|--------|
| **模型原生型** | 真正训练垂类基础/科学模型 | Isomorphic(IsoDDE)、华佗GPT、BloombergGPT、GNoME、Hippocratic、Cursor(Tab) | 模型能否持续领先 + 数据/反馈独占 |
| **模型系统型** | 自研专用模型 + 编排 | Cognite、XBOW、Abnormal AI、Abridge、Med-PaLM 2 | 模型可替换，系统闭环与行动权难替换 |
| **工作流应用型** | 主要调用通用模型 + RAG/Agent | Harvey、Sierra、Decagon、Hebbia、AlphaSense、Rogo | 商业化强，但需防基础模型上下夹击 |

**关键判断**：本数据集里综合分最高的模型（度小满轩辕 96、GNoME 93、ChatLaw 93）多为模型原生型且有论文支撑；而工作流应用型（Harvey 86、Sierra 71）虽商业化领先，但模型可替换性高，护城河更依赖分发和工作流。

---

## 3. 各 Tier 1 领域深度

### 3.1 金融（10 个高质量模型，最成熟）
- **模型原生型**：BloombergGPT(83，50B 参数，arXiv 论文)、度小满轩辕(96，MoE + 双奖励 RL)、蚂蚁百灵(MoE)
- **工作流应用型**：AlphaSense(86，$30T AUM 客户)、Hebbia、Rogo、Eilla(M&A)
- **专项**：Shift/Tractable/CAPE Analytics(保险理赔视觉)
- 商业模式：终端订阅（Bloomberg）、企业年合同（AlphaSense/Rogo）
- 数据可信度：BloombergGPT 有论文，其余多为自报

### 3.2 法律（9 个，商业化最快）
- **模型原生型**：ChatLaw(93，MoE + LawBench 超 GPT-4)、AC GLM-5.1(Harvey Legal Agent，89)
- **工作流应用型**：Harvey(86，多模型路由)、CoCounsel(91，Westlaw 内容)、Eudia(企业法务)、Norm Ai(合规)、EvenUp(人身伤害)
- 关键洞察：法律文本能力易被通用模型追平，真正壁垒是**权威内容库(CoCounsel)**、**分发(Harvey)**、**专有数据集(EvenUp 250K+ 判决)**

### 3.3 医疗（10 个）
- **模型原生型**：华佗GPT(91，cMedQA2)、Hippocratic(Polaris constellation)、Med-PaLM 2(84)
- **模型系统型**：Abridge(88，300+ 医疗系统)、Nabla(85)、PathAI(病理)
- 强闭环候选：Abridge（临床对话→医生修订→EHR→编码→支付）
- 数据可信度：华佗GPT/Med-PaLM 有论文，Abridge/Hippocratic/Nabla 全为自报

### 3.4 药物研发（8 个，最可能形成模型级壁垒）
- **模型原生型**：Isomorphic IsoDDE(87，AlphaFold 血统)、insitro(因果 AI)、Recursion(82)
- 特点：模型输出直接影响药物设计，实验反馈昂贵且独占——报告判断此领域最可能出现真正的模型级护城河
- 商业模式：药企合作预付款 + 里程碑 + 版税（非席位订阅）

### 3.5 材料科学（8 个）
- **模型原生型**：GNoME(93，Nature 论文 + 736 种实验验证)、MatterGen(扩散生成)
- 自主实验室：Chemify/Kebotix/Atinary/Aionics(self-driving lab)
- GNoME 是本数据集少数有第三方实验验证的模型（third-party source），可信度最高

---

## 4. 商业模式谱系

| 模式 | 代表 | 趋势 |
|------|------|------|
| 席位/订阅 | Bloomberg、AlphaSense、Cursor | Agent 自动化越深，seat 逻辑越弱 |
| 企业年度合同 | Abridge、Harvey、Cognite、Rogo | 主流，靠多流程渗透扩张 |
| 按结果计费 | Sierra、Decagon（客服）、XBOW（按渗透测试） | 最能体现价值，承担归因风险 |
| 里程碑/版税 | Isomorphic、insitro、Recursion（药物） | 上行空间最大，兑现周期最长 |

---

## 5. 数据可信度分析（关键警示）

本数据集 343 条 benchmark 的来源分布：

| 来源 | 条数 | 占比 | 含义 |
|------|:---:|:---:|------|
| self-reported | 314 | **91.5%** | 公司自报，未审计 |
| paper | 17 | 5.0% | 论文/同行评审 |
| leaderboard | 8 | 2.3% | 公开排行榜 |
| third-party | 4 | 1.2% | 第三方验证 |

**结论**：垂类 AI 领域几乎没有性能数据经过独立验证。使用本报告或任何垂类 AI 宣传数据时，应清醒认识到绝大多数"性能领先""ROI 提升"来自厂商自身口径。**有论文或第三方验证的模型（如 GNoME、BloombergGPT、ChatLaw、华佗GPT、FengWu）可信度显著更高。**

---

## 6. 战略判断

1. **优先物理世界/实验/交易结果反馈的领域**：药物研发、材料科学、气象（Tomorrow.io 卫星数据）、工业——这些领域数据难从公开互联网获得，模型级壁垒更可能成立。

2. **警惕纯文本工作流领域的同质化**：法律、金融研究、客服的输入输出主要是文本，通用模型追赶最快，护城河须建立在专有数据、工作流控制和结果反馈上。

3. **模型原生 ≠ 商业赢家**：ChatLaw(93)技术最强但商业化弱于 Harvey(86)；Harvey 靠分发和工作流领先却用可替换的多模型。二者说明**技术领先和商业领先是两条不同的曲线**。

4. **数据可信度是被系统性忽视的风险**：91.5% 自报率意味着行业普遍缺乏独立验证。投资/采购决策应优先看有第三方验证或论文支撑的模型。

---

## 附录：报告方法与局限

- **数据来源**：本仓库 `domains/**/*.yaml`，每个模型含 raw 原始资料（`data/raw/`）可回溯
- **质量筛选**：用 `scripts/check.py` 三维度评分，仅纳入综合 ≥70 的 90 个模型
- **排除的 20 个**：综合分 <70（Eudia 63、Palantir AIP 66、MatterGen 67、Abnormal AI 69 等），多因来源单一或技术数据不足，非公司本身价值低
- **局限**：
  1. 本数据集偏重能公开搜到信息的公司，遗漏纯内部模型
  2. benchmark 91.5% 为自报，性能对比仅供参考
  3. 领域覆盖不均（金融/法律/医疗密集，政务/软件开发稀疏）
  4. 数据快照于 2026-08，模型和公司信息变化快
