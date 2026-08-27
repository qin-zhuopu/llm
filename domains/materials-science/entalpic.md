---
title: "Entalpic — AI-for-Science 材料发现引擎与 LeMaterial 数据集"
date: "2026-08-27"
source: "https://entalpic.ai"
---

# Entalpic

Entalpic 是一家总部位于法国巴黎（并在加拿大蒙特利尔设点）的 AI-for-Science 初创公司，使命是「掌握基础化学以走向更高效、更可持续的未来」，聚焦于能源密集型工业的净零转型。团队由机器学习、化学与材料专家组成，超过 50% 拥有博士学位，成员来自 Intel、Air Liquide、Applied Materials、Meta、Google、Amazon。

## 高通量发现引擎

Entalpic 的高通量发现引擎能快速筛选庞大化学空间，在真实工业约束下识别可行材料候选，重点应用方向：

- 薄膜与涂层：原子级精度决定工艺良率与器件可靠性
- 电池：优化正极活性材料、表面涂层与界面化学以提升电池性能
- 催化：设计催化表面与活性位点，最大化活性、选择性与工业稳定性
- 半导体：设计沉积工艺所需的新前驱体与特种化学品

## LeMaterial（与 Hugging Face 合作的开源材料数据生态）

LeMaterial 是 Entalpic 与 Hugging Face 联合发起的开源材料研究项目，目的是简化并加速材料研究：更易训练 ML 模型、识别新材料、探索化学空间。

- LeMat-Bulk 数据集：统一、清洗并标准化 Materials Project、Alexandria、OQMD 三大主流材料数据库，形成单一协调格式，含 **6.7M 条目、7 种材料属性**，基于 Optimade 标准，采用 CC-BY-4.0 许可。
- 材料指纹（hashing function）：Entalpic 提出通过哈希函数为每个材料分配唯一标识——先用成键算法（如 EconNN）从晶体结构提取图，再用 Weisfeiler-Lehman 算法计算哈希，结合成分与空间群信息形成指纹，用于快速判定材料是否新颖、去重、跨数据库连接。速度远快于 Pymatgen 的 StructureMatcher（Carbon-24：100 秒 vs 17 小时；MPTS-52：330 秒 vs 4.9 小时）。
- ML 模型：在 LeMat-Bulk 上训练机器学习原子间势（MLIP），如 EquiformerV2、FAENet。未来发布计划包含 r2SCAN 数据、OC20/OC22 表面数据集、MPTrj、OMat24 轨迹数据。

指纹与数据集工作得到 Meta 的 Zachary Ulissi、Luis Barroso-Luque 及 Newfound Materials 的 Matt McDermott 反馈支持。

## 定位

Entalpic 属于「模型原生型 + 模型系统型」：既构建材料发现的高通量筛选引擎，也开源材料数据基础设施（LeMaterial/LeMat-Bulk）与预训练 MLIP 模型，商业上服务能源密集型工业客户。

---

来源：
- Entalpic 官网 https://entalpic.ai （获取日期 2026-08-27）
- LeMaterial 博客（Hugging Face）https://huggingface.co/blog/lematerial （获取日期 2026-08-27）
