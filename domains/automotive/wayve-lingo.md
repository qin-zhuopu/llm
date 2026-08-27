# Wayve LINGO

> 来源: [https://wayve.ai/thinking/lingo-2-driving-with-language/](https://wayve.ai/thinking/lingo-2-driving-with-language/)
> 抓取时间: 2026-08-25
> 公司: Wayve

---

LINGO-2 is a closed-loop vision-language-action model (VLAM) for autonomous driving developed by Wayve, a British AI company specializing in embodied AI for assisted and automated driving. Announced on April 17, 2024, LINGO-2 is the first driving model trained on natural language that has been tested on public roads, capable of both driving a car and simultaneously explaining its decisions in real time.

## Architecture

LINGO-2 integrates three fundamental components into a unified driving model:

### Vision Module
The Wayve vision model processes camera inputs to perceive the driving environment, identifying road geometry, traffic participants, signals, and other scene elements relevant to navigation.

### Language Module
An auto-regressive language model generates natural language descriptions and reasoning about driving decisions. This provides continuous commentary on the model's motion planning choices, making the autonomous driving system interpretable and transparent.

### Action Module
The action component produces driving control outputs (steering, acceleration, braking) based on the combined vision and language understanding, creating a complete closed-loop driving system.

## Key Innovations

### Closed-Loop Integration
Unlike previous approaches that treated language as a post-hoc explanation layer, LINGO-2 integrates language directly into the driving loop. Language both informs and reflects driving behavior, creating a bidirectional relationship between verbal reasoning and physical actions.

### Real-Time Natural Language Commentary
LINGO-2 provides visibility into the decision-making process of the driving model through continuous natural language explanations. The system can articulate why it is making specific maneuvers, what hazards it has identified, and what it anticipates in the environment.

### Customization and Control
By connecting language to driving actions, LINGO-2 opens a new dimension of control and customization for the autonomous driving experience. Instructions can be given in natural language to influence driving style and behavior.

## Evolution from LINGO-1

LINGO-2 builds upon the LINGO-1 series:
- **LINGO-1**: An open-loop driving commentator that could explain driving scenes but did not influence driving behavior
- **LINGO-1-X**: Extended the vision-language model to VLX (vision-language-X) domain with reference segmentation capabilities
- **LINGO-2**: The first fully closed-loop VLAM that combines vision, language, and action in a single integrated system

## Research Contributions

Wayve has also released LingoQA, a benchmark dataset designed to evaluate whether models can describe scene elements, predict future actions, explain justifications, and indicate attention focus areas. This benchmark supports the broader research community in developing interpretable autonomous driving systems.

## Significance

LINGO-2 represents a paradigm shift in autonomous driving by demonstrating that natural language can serve as both an interface for human understanding and a functional component of the driving system itself. This approach enables more transparent, controllable, and trustworthy autonomous vehicles.

---

> 补充来源: [Driving with LLMs: Fusing Object-Level Vector Modality for Explainable Autonomous Driving (arXiv 2310.01957)](https://arxiv.org/abs/2310.01957)
> 抓取时间: 2026-08-30

## 技术溯源论文（Wayve）

Wayve 团队的 arXiv 论文《Driving with LLMs》(2310.01957) 是 LINGO 系列视觉-语言-动作模型的技术基础。论文提出一种对象级多模态 LLM 架构，将向量化数值模态与预训练 LLM 融合以增强驾驶情境理解；构建了源自 1 万个驾驶场景的 16 万条 QA 对数据集（控制指令由 RL agent 采集、问答由 teacher LLM GPT-3.5 生成），并提出 Driving QA 评估指标。该数据集与评测方法与 Wayve 后续发布的 LingoQA 基准一脉相承，论文结论指出基于 LLM 的驾驶动作生成相较传统行为克隆更具泛化与可解释潜力。

