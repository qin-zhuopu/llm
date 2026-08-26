# Applied Compute Agent Cloud (AC2)

## 概述

Applied Compute 是一家专注于 Specific Intelligence（特定智能）的企业级 AI 训练与推理平台公司。公司由三位前 OpenAI 研究员于 2025 年 10 月创立，融资总额 $160M，估值 $1.3B。

核心理念：帮助企业构建和拥有自己的专属 AI 模型和智能体，而非依赖通用大模型 API。采用嵌入式工程团队模式，与客户肩并肩工作。

## 创始团队

- **Yash** - Co-founder，前 OpenAI 研究员，Codex（代理式软件工程师）核心成员
- **Rhythm** - Co-founder，前 OpenAI 研究员，o1（首个 RL 训练推理模型）核心贡献者
- **Linden** - Co-founder，前 OpenAI 研究员，ML 系统与 RL 训练基础设施

团队三分之二成员为前创始人，技术背景涵盖顶级 AI 研究者和数学奥林匹克获奖者。

## 融资历程

- **总融资**: $160M
- **最新轮估值**: $1.3B post-money
- **投资方**: Kleiner Perkins（最新轮领投）、Benchmark、Sequoia、Lux、Elad Gil、Greenoaks、Neo、Hanabi、Victor Lazarte、Omri Casspi 等

## 平台能力: AC2 (Applied Compute Agent Cloud)

AC2 是 Applied Compute 内部研究员使用的同一套平台，现在也开放给客户使用。

### 训练能力

- **全参数 RL 后训练** - 不限于 LoRA，支持对整个模型权重进行强化学习优化
- **LoRA 微调** - 轻量级适配方案
- **On-policy 自蒸馏** - 利用生产流量进行持续学习，即使原始环境无法回放
- **支持所有最新开源模型** - 客户可选择合适的基座模型
- **自带 Harness** - 客户可使用自己的训练代码和评估框架，几十行代码即可开始训练
- **RL 控制平面** - 自动适配计算规模和上下文长度，新增计算资源立即实现高利用率

### 推理能力

- **专属推理部署** - 为客户工作负载端到端优化
- **训练-推理一致性** - 生产端点使用与训练相同的采样配置、数值精度和内核
- **自动扩缩容** - 99.9% 可用性，根据流量自动调整副本数
- **推测解码** - 低延迟推理
- **热更新** - 新 checkpoint 可在几分钟内部署到相同端点，无需更改 API

### Ari (Applied Research Intelligence)

Ari 是 AC2 平台内置的 AI 研究助手，功能包括：
- 自动监控训练 run 健康状态
- 分析数千条 agent trace，发现异常行为
- 跨实验记忆项目经验
- 生成结构化报告和图表
- 自动启动新实验修复问题
- Slack 集成，实时通知研究员

### 安全与合规

- SOC 2 认证
- ISO 42001 认证
- 客户拥有模型和数据
- 在客户自有安全环境中运行

## 客户案例

| 客户 | 领域 | 应用 |
|------|------|------|
| Harvey | 法律 | 法律智能体（LAB 评测超越 GPT-5.5/Opus 4.8）、文档审查模型 |
| DoorDash | 零售/外卖 | 菜单错误修正模型，低质量菜单减少 30% |
| Cognition (Devin) | 代码 | 代码智能体模型训练 |
| Mercor | HR/招聘 | 人力资源智能体 |
| NVIDIA | 硬件/AI | 模型训练合作 |
| Microsoft | 科技 | 定制模型 |

## 差异化特点

1. **非通用 API 平台** - 不提供公开模型调用，专注帮客户训练自有模型
2. **嵌入式服务** - 工程师嵌入客户团队，不委派不外包
3. **客户拥有一切** - 模型权重、数据、训练环境都属于客户
4. **持续改进闭环** - 生产数据反馈到训练，模型越用越好
5. **前沿研究能力** - 团队来自 OpenAI 核心项目，具备 frontier model 训练经验

## 参考链接

- [Applied Compute 官网](https://www.appliedcompute.com)
- [AC2 Platform 介绍](https://appliedcompute.com/platform/introducing-ac2)
- [Ari 研究助手介绍](https://appliedcompute.com/platform/ari)
- [融资公告](https://appliedcompute.com/company/fundraise)
- [公司介绍](https://appliedcompute.com/company/its-time-to-get-specific)
- [Harvey 案例](https://appliedcompute.com/case-studies/harvey)
- [DoorDash 案例](https://appliedcompute.com/case-studies/doordash)
- [Mercor 案例](https://appliedcompute.com/case-studies/mercor)
