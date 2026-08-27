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
