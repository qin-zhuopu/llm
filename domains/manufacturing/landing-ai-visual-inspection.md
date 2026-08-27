# LandingAI (LandingLens) — 工业视觉质检平台

> 来源: https://landing.ai/
> 抓取日期: 2026-08-27

LandingAI 由吴恩达（Andrew Ng，Google Brain 创始人、百度首席科学家、Coursera 联合创始人）创立，是"数据中心 AI"(data-centric AI) 理念的开创者。其面向工业制造的旗舰产品 **LandingLens** 是一个计算机视觉平台，让制造工程师用小数据集构建、部署并持续改进深度学习缺陷检测模型。

## 定位

- **模型系统型 / 工作流应用型**：自研专有视觉模型 + 数据中心工作流平台。
- 核心思想：工业缺陷检测任务数据量小（几十到几百张图），杠杆在于系统化提升数据质量与标注一致性，而非堆模型规模。

## 核心产品

- **LandingLens**：端到端工业视觉质检平台（数据标注 → 云端训练 → 边缘部署 LandingEdge → 持续改进）。支持分类、目标检测、分割、异常检测。
- **Agentic Document Extraction (ADE)**：视觉优先的文档结构化抽取，带置信度评分和可审计溯源，每分钟处理数千页。
- **VisionAgent**：Agentic 计算机视觉应用构建工具。

## 技术特点

- 底层为 CNN / 视觉 Transformer 深度网络，用于图像分类、目标检测和分割。
- 数据中心 AI：通过更好的、经过策展的数据提升精度；失败样本被捕获、审计并系统性反馈以减少错误和返工。
- Agentic 编排：针对每个文档/检测任务自适应规划、决策、验证，直到满足质量阈值。
- 部署：云端 GPU 训练 + 边缘 CPU/GPU 推理；与工厂摄像头和 PLC 集成实现在线 pass/fail 信号。

## 商业数据

- 50+ 企业客户；已处理 10 亿+ 图像和文档；处理时延 <2 秒。
- 2021 年完成 5700 万美元 A 轮融资（McRock Capital、Insight Partners 领投）。
- 企业级安全：SOC 2 Type II、GDPR & HIPAA 合规；云/本地/VPC 部署；零数据保留选项。
- 提供 REST API 及 Python / TypeScript SDK。
