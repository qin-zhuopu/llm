# NVIDIA Alpamayo 2 Super

> 来源: [https://developer.nvidia.com/drive](https://developer.nvidia.com/drive)
> 抓取时间: 2026-08-27
> 公司: NVIDIA

---

NVIDIA Alpamayo 2 Super 是 NVIDIA DRIVE 自动驾驶生态中的推理基础模型。NVIDIA 提供从传感器数据整理、合成数据生成、模型训练、闭环仿真到量产级车载算力的端到端栈。

## 技术定位

- **34B VLA 推理基础模型**：Alpamayo 2 Super 是一个开放的 340 亿参数 视觉-语言-动作 (Vision-Language-Action, VLA) 推理基础模型，含 RL 后训练、灵活的多摄像头支持与导航引导，用于自动驾驶车辆轨迹规划。
- **开放后训练**：SFT 与 RL 微调的后训练脚本以 Apache 2.0 许可在 GitHub 开放，可在专有车队数据上微调。
- **AlpaGym**：业内首个用于在 GPU 规模上训练 AV 策略模型的模块化 RL 框架，让模型在连续决策-观测循环中暴露静态数据集无法发现的累积误差。
- **AlpaSim**：开源闭环 AV 仿真框架，微服务架构把渲染、物理、交通行为、策略执行分配到不同 GPU 资源，支持 Omniverse NuRec 与 Cosmos-Dreams 作为渲染后端。

## 配套 NVIDIA AV 组件

- **DRIVE AGX (Orin, Thor)**：车规级车载算力，DriveOS SDK（DriveWorks、CUDA、TensorRT）。
- **Cosmos Curator / Cosmos Reason VLM**：多模态数据整理。
- **CoC 自动标注管线**：为驾驶片段自动生成因果链 (Chain of Causation) 推理标签。
- **Omniverse NuRec**：基于高斯方法把真实驾驶数据重建为可交互仿真。
- **Cosmos Transfer**：世界基础模型，从 HD 地图、激光雷达深度与文本提示生成照片级合成驾驶数据。

## 能力

- 基于推理的自动驾驶轨迹规划
- 视觉-语言-动作多模态推理
- 灵活多摄像头输入支持
- 导航引导下的驾驶决策
- 专有车队数据上的 SFT + RL 微调
- 配合 AlpaSim 闭环仿真评估策略

---

> 补充来源: [NVIDIA Research — Autonomous Vehicle Research Group (Alpamayo, AlpaSim, PhysicalAI-AV)](https://research.nvidia.com/labs/avg/)
> 抓取时间: 2026-08-30

## NVIDIA 研究团队背景

NVIDIA Research 自动驾驶研究组（由 Marco Pavone 博士领导）发布了 **Alpamayo 1**，被描述为「全球首个用于自动驾驶研究的开放推理 VLA（视觉-语言-动作）模型」，并配套发布 **AlpaSim**（模块化、轻量、数据驱动的感知仿真器）以及 **PhysicalAI-AV** 数据集，共同构成面向端到端自动驾驶的数据、模型与闭环评估工具生态。研究方向涵盖下一代 AV 架构（可微/半模块化/端到端栈）、AV 基础模型（视觉-语言基础模型、VLA 建模、开放场景理解）、仿真（行为/交通建模、语言驱动仿真生成、神经仿真器）与 AV 的 AI 安全（不确定性量化、在线监控、神经架构中的规则推理、安全 KPI 验证），并与 NVIDIA DRIVE 产品团队紧密协作。
