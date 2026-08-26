# Hippocratic AI

> 来源: [https://www.hippocratic.ai](https://www.hippocratic.ai)
> 抓取时间: 2026-08-25
> 公司: Hippocratic AI

---

Hippocratic AI是一家总部位于美国加州帕洛阿尔托的人工智能公司，专注于构建面向医疗健康领域的安全性优先的大语言模型（LLM）。公司以医学伦理中的"首先，不伤害"（Hippocratic Oath）为核心理念，致力于开发用于非诊断性、面向患者的临床任务的生成式AI智能体。

## 融资历程

Hippocratic AI已完成多轮大规模融资，累计融资总额超过4亿美元：
- **种子轮**：筹集约5000万美元
- **A轮**（2024年3月）：由Premji Invest和General Catalyst领投，融资5300万美元，估值5亿美元
- **B轮**（2025年1月）：由Kleiner Perkins领投，融资1.41亿美元，估值16.4亿美元，正式进入独角兽行列
- **C轮**（2025年11月）：由Avenir Growth领投，融资1.26亿美元，估值35亿美元
- 投资方包括NVIDIA NVentures、a16z、General Catalyst等知名机构

## 核心技术

### Polaris架构
Hippocratic AI的核心技术平台名为Polaris，采用安全性优先的LLM星座架构（constellation architecture），专为医疗场景设计。该系统能够创建AI智能体，与患者进行自然对话，处理非诊断性话题。

### 定制化语音识别
公司与NVIDIA合作，开发了针对临床医患对话场景微调的自动语音识别（ASR）技术，能够准确理解医疗术语和患者口语化表达。

## 应用场景

- **患者导航**：帮助患者了解就医流程、保险覆盖范围和预约安排
- **用药提醒**：智能提醒患者按时服药，解答药物相关疑问
- **营养咨询**：为患者提供个性化的饮食建议和营养指导
- **出院后随访**：自动进行出院后的健康状况跟踪和康复指导
- **慢病管理**：协助慢性病患者进行日常健康管理
- **术前准备指导**：为即将接受手术的患者提供准备说明

## 商业模式

Hippocratic AI采用创新的"AI智能体人力市场"模式，医疗系统可以按需"雇佣"AI智能体来执行特定的低风险、患者面向的工作任务，帮助缓解全球医疗专业人员短缺问题。

## 安全性设计

作为安全性优先的医疗AI，Hippocratic AI在设计中严格区分诊断性和非诊断性任务，AI智能体仅处理不涉及医学诊断的患者交互场景。公司采用多阶段安全测试流程，确保AI输出的安全性、准确性和共情能力。

---

> 补充来源: [https://arxiv.org/abs/2403.13313](https://arxiv.org/abs/2403.13313)
> 日期: 2025-06-17

## Polaris技术架构详情 (论文: arXiv:2403.13313)

### 模型规模与架构
- 总参数规模: 1万亿参数(one-trillion parameter constellation system)
- 由多个数十亿参数级LLM组成协作智能体系统
- 有状态主智能体(stateful primary agent): 驱动对话参与度
- 多个专业支持智能体(specialist support agents): 执行护士级医疗任务，提高安全性、减少幻觉

### 训练方法
- 复杂的迭代式协同训练协议(iterative co-training)
- 多智能体优化多样化目标(安全性、对话质量、共情等)
- 使用专有数据、临床护理计划、医疗监管文件、医学手册训练
- 使用有机医患对话和模拟对话(患者演员与资深护士)对齐专业说话风格
- 与NVIDIA合作开发临床对话场景微调的ASR

### 评测结果
- 招募1100+美国注册护士和130+执业医师进行端到端对话评估
- Polaris在以下维度与人类护士表现持平:
  - 医疗安全(medical safety)
  - 临床准备度(clinical readiness)
  - 对话质量(conversational quality)
  - 床旁态度(bedside manner)
- 专业支持智能体显著优于GPT-4和LLaMA-2 70B
