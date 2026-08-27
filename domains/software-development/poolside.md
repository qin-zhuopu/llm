---
title: Poolside — 面向软件工程的专用基础模型
date: 2026-08-27
source: https://poolside.ai
---

# Poolside — 面向代码/软件工程的专用基础模型

> 来源: https://poolside.ai ，https://en.wikipedia.org/wiki/Poolside_AI
> 抓取日期: 2026-08-27

Poolside AI 是一家美国 AI 公司，**专门为软件与编码应用训练大语言模型**（而非通用任务）。属于典型的**模型原生型**垂类公司：自研面向代码的基础模型 + 自主软件开发产品。

## 公司与团队
- 2023 年初创立，创始人 Jason Warner（GitHub 前 CTO，President & Co-Founder）与 Eiso Kant（CTO & Co-Founder）。
- 约 150 名员工（2025-12），分布美/英/法；总部旧金山，巴黎设分部。
- Project Horizon：位于德州 Pecos County 的 2 吉瓦 AI 园区，2025-10 启动一期，为美国最大数据中心之一。

## 技术
- 模型**专为软件开发设计**，用开发者的自然语言 prompt 生成并测试代码。
- **Model Factory**：Poolside 训练与评估模型的系统，涵盖 GPU-to-GPU 权重传输、自动化架构消融（architecture ablations）、以及**大规模从代码执行中做强化学习（reinforcement learning from code execution at scale）**。
- 2026-07 发布 **Laguna S 2.1**：118B 参数开源权重（open-weights）代码大模型，OpenMDW 许可；被 Forbes/TNW 视为"西方对 DeepSeek/Qwen 的回应"。co-CEO Warner 表示还将开发更大模型。
- 2024-12 与 AWS 合作，通过 Amazon Bedrock 与 EC2 提供其基础模型，支持企业在自有 AWS 环境部署。

## 商业数据
- 首年种子轮 $26M，随后追加 $100M。
- 2024-10 Series B $500M（Bain Capital、DST Global、eBay 等领投），估值 $3B。向投资人演示时用 prompt "Write me the code for a snake video game in python"。
- 2025-10 NVIDIA 宣布投资至多 $1B，估值翻两番至 **$12B**。
- 已与美国国防部（DoD）、RTX Corporation 等美国国防工业客户签约。

## 定位
模型原生型：真正训练面向代码的基础模型（Laguna S 系列），并在其上构建自主软件开发引擎，与通用模型公司差异化明显。
