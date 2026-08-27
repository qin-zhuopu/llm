---
title: "Mattiq — 面向材料的实验数据引擎 (The Data Engine for Materials)"
date: "2026-08-27"
source: "https://www.mattiq.com"
---

# Mattiq

Mattiq 自称「面向材料的数据引擎」(The Data Engine for Materials)，核心主张是：「我们需要的材料尚不存在，Mattiq 生成让 AI 预测变为现实的 ground truth（真值）。」

## 定位：为材料 AI 补上「实验真值」这一层

材料 AI 面临「现实问题」：今天的模型大量基于仿真训练，因而继承了仿真中的近似与偏差。Mattiq 通过大规模高通量物理实验生成实验真值，为材料智能补上缺失的实验层，让上层的工业 R&D、AI 与自主实验室都更具预测性。

## 材料前沿方向（已在催化验证，快速扩展）

1. 电化学（Electrochemistry）：在百万级候选催化剂空间中绘制活性与耐久性——用于制氢、燃料电池、CO2 转化
2. 磁体（Magnets）：筛选成分的矫顽力、各向异性与热稳定性——包括无稀土磁体（用于牵引电机、机器人、国防）与记录介质
3. 电池（Batteries）：将成分与工艺关联到离子输运、稳定性与界面行为——电极与电解质真值
4. 存储器（Memory）：筛选开关、保持、耐久与变异性——阻变、相变、铁电存储材料
5. 超导材料（Superconducting Materials）：在庞大多元体系中绘制相形成、结构与掺杂——用于聚变磁体、电力、高场系统
6. 半导体材料（Semiconductor Materials）：筛选漏电、电阻率与稳定性——介电层、氧化物半导体、互连金属

## 起源与团队

- 源自西北大学 Chad Mirkin 教授开创的 Megalibrary 技术（可在单一芯片上并行合成数百万种材料组合）。
- Prof. Chad Mirkin — Scientific Founder & Director；Ben Schlatka — CEO & Director；Dr. Andrey Ivankin — Co-Founder & CTO；Alex Mantis — Director of Data & AI；Dr. Carolin Wahl — Director of R&D。
- 投资方：Material Impact、CS Venture（Carmichael Roberts、Quinten Stevens）。

## 定位

Mattiq 属于「模型系统型/数据基础设施型」：以高通量实验平台生成材料实验真值数据集，为材料 AI/MLIP 模型提供训练与验证的地面真值层，是材料基础模型生态的关键上游。

---

来源：
- Mattiq 官网 https://www.mattiq.com （获取日期 2026-08-27）

---

## 补充：科学基础（Chad Mirkin / Megalibrary，第二来源）

> 来源: https://en.wikipedia.org/wiki/Chad_Mirkin ｜ 抓取日期: 2026-08-27

Mattiq 的科学创始人是西北大学化学教授 Chad Mirkin（国际纳米技术研究所所长），其"材料数据引擎"建立在 Mirkin 首创的 Megalibrary 技术之上——组合式合成与高通量筛选海量材料空间，为材料 AI 生成实验"ground truth"。Mirkin 发表逾 940 篇论文，Google Scholar H-index 约 210，逾 1,400 项专利，同时入选美国科学院、工程院、医学院三院。Mattiq 应用覆盖催化（电化学：氢能、燃料电池、CO₂ 转化）、磁体、电池、存储器、超导材料、半导体材料。公司不公开模型参数或独立基础模型；可信技术基础是 Mirkin 课题组（发表于 Science）的学术积淀。
