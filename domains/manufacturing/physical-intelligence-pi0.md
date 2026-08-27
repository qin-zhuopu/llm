# Physical Intelligence (π0 / π0.5 / π*0.6 / π0.7) — 机器人基础模型

> 来源: https://physicalintelligence.company/ , https://www.physicalintelligence.company/blog/pi0
> 抓取日期: 2026-08-27

Physical Intelligence（π）致力于把通用 AI 带入物理世界，开发能"控制任何机器人做任何任务"的机器人基础模型——直接关联制造自动化、装配、物料搬运和工厂机器人。

## 定位

- **模型原生型**：真正训练视觉-语言-动作（VLA）基础模型；π0 已开源权重，后续 π0.5/π*0.6/π0.7 为更强的闭源/内部模型。

## 模型谱系

- **π0**（2024-10）：首个通才策略——基于预训练视觉-语言模型 + 动作专家的 VLA 流模型；2025-02 开源权重和代码，附 π0-FAST 自回归变体。
- **π0.5**（2025-04）：扩展 π0，具备开放世界泛化；可控制移动机械臂清理全新厨房或卧室。
- **π*0.6**（2025-11）：从经验中学习的 VLA，用 RL 训练以提升真实任务的成功率和吞吐。
- **π0.7**（2026-04）：可引导（steerable）模型，具涌现能力，泛化出现阶跃式提升。

## 技术特点（π0，来自公开论文 arXiv:2410.24164）

- 架构：视觉-语言-动作（VLA）模型，构建于预训练视觉-语言模型 **PaliGemma（约 3B）** 之上，增加动作专家（action expert）；总参数约 **3.3B**。
- 使用 **flow matching（流匹配，扩散的一种变体）** 表示连续动作分布，实现高频灵巧控制（最高 50 Hz）。
- 在跨形体（cross-embodiment）大数据集上训练，覆盖 7+ 种机器人配置和 68 个任务，加上 Open X-Embodiment 数据集。
- 动作分块（action chunking）+ 实时推理实现平滑操作。
- π*0.6 加入来自真实世界经验的强化学习（"Recap" 方法）以提升吞吐/成功率。

## 研究主题

- Multi-Scale Embodied Memory (MEM)：长短期记忆，支持超过 10 分钟的任务。
- Real-Time Action Chunking (RTC)：大型 VLA 在高延迟下的实时动作分块。
- 人到机器人迁移；RL Token 抽取用于快速在线 RL。

## 商业数据

- 2024 年成立；融资约 4 亿美元、估值约 24 亿美元，后续报道更高轮次（约 6 亿美元+）。
- 投资方：Bond、Jeff Bezos、Khosla Ventures、Lux Capital、OpenAI、Redpoint Ventures、Sequoia Capital、CapitalG、Thrive Capital。
