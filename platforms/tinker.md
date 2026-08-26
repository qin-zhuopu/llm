# Tinker (Thinking Machines Lab)

## 概述

Tinker 是 Thinking Machines Lab 推出的 AI 推理与训练平台。Thinking Machines Lab 由前 OpenAI CTO Mira Murati 于 2025 年 2 月创立，获得 a16z 领投的 $2B 种子轮融资，估值达 $12B，团队规模约 212 人。

平台核心提供两大服务：
1. **训练 API** - 支持 28+ 模型的 LoRA 微调，训练方法涵盖 SFT、RL、DPO、蒸馏
2. **推理 API (Beta)** - 提供自研 Inkling 系列模型的 Serverless 推理服务

## 推理 API

推理 API 目前处于 Beta 阶段，提供以下模型：

| 模型 | 参数量 | 上下文 | 模态 | 输入价格 | 输出价格 |
|------|--------|--------|------|----------|----------|
| Inkling | 975B MoE | 64K/256K | Hybrid+Audio+Vision | $1.00/M | $4.05/M |
| Inkling-Small | 276B MoE | 64K/256K | Text | $0.30/M | $1.20/M |

**Inkling** 是 Thinking Machines Lab 的旗舰模型，975B MoE 架构，支持文本、视觉和音频多模态输入，最大上下文窗口 256K tokens。

**Inkling-Small** 是轻量版本，276B MoE 架构，专注文本处理，同样支持 256K 上下文。

## 训练 API

训练 API 支持 28+ 模型的微调，采用 LoRA 方法，支持的训练方式包括：
- **SFT** (Supervised Fine-Tuning)
- **RL** (Reinforcement Learning)
- **DPO** (Direct Preference Optimization)
- **蒸馏** (Distillation)

### 可微调模型列表

| 模型 | 参数量 | 架构 | 上下文 | 特点 |
|------|--------|------|--------|------|
| Inkling | 975B MoE | MoE | 64K/256K | 多模态旗舰 |
| Inkling-Small | 276B MoE | MoE | 64K/256K | 轻量版 |
| Nemotron-3.5-Lightning-30B-A3B | 30B MoE | MoE | - | - |
| Nemotron-3-Ultra-550B-A55B | 550B MoE | MoE | - | - |
| Nemotron-3-Super-120B-A12B | 120B MoE | MoE | - | - |
| Nemotron-3-Nano-30B-A3B | 30B MoE | MoE | - | - |
| Kimi-K2.6 | Large MoE | MoE | 32K/128K | - |
| Qwen3.8-27B | 27B Dense | Dense | 64K/256K | Medium Dense |
| Qwen3.6-35B-A3B | 35B MoE | MoE | - | Medium MoE |
| Qwen3.5-397B-A17B | 397B MoE | MoE | - | Large MoE |
| Qwen3.5-35B-A3B-Base | 35B MoE | MoE | - | Base模型 |
| Qwen3.5-9B / 9B-Base | 9B Dense | Dense | - | Small Dense |
| Qwen3.5-4B | 4B Dense | Dense | - | Compact Dense |
| Qwen3-8B | 8B Dense | Dense | - | Small Dense |
| GPT-OSS-120B | 120B MoE | MoE | 32K/128K | Reasoning |
| GPT-OSS-20B | 20B MoE | MoE | - | Reasoning |
| DeepSeek-V3.1 | Large MoE | MoE | - | - |

### 训练定价 (per million tokens)

- 最便宜: GPT-OSS-20B - $0.396/M train tokens
- 最贵: Inkling 256K - $11.23/M train tokens

## 公司背景

- **公司**: Thinking Machines Lab
- **创始人**: Mira Murati (前 OpenAI CTO)
- **成立时间**: 2025 年 2 月
- **融资**: $2B 种子轮 (a16z 领投)
- **估值**: $12B
- **团队**: ~212 人

## 参考链接

- [Tinker Platform](https://thinkingmachines.ai/tinker/)
- [Thinking Machines Lab](https://thinkingmachines.ai/)
