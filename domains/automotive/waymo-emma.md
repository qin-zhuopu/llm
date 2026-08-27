# Waymo EMMA

> 来源: [https://waymo.com/blog/2024/10/introducing-emma](https://waymo.com/blog/2024/10/introducing-emma)
> 抓取时间: 2026-08-27
> 公司: Waymo

---

EMMA (End-to-End Multimodal Model for Autonomous Driving) 是 Waymo 于 2024 年 10 月发布的端到端自动驾驶研究模型，由 Google 多模态大模型 Gemini 驱动。EMMA 采用统一的端到端训练模型，直接从传感器数据生成自动驾驶车辆的未来轨迹，并针对自动驾驶任务专门训练和微调，借助 Gemini 广博的世界知识理解复杂道路场景。

## 技术要点

- **端到端学习**：EMMA 处理原始摄像头输入与文本数据，生成多种驾驶输出，包括规划轨迹、感知目标和道路图元素。
- **统一语言空间 (Unified Language Space)**：把非传感器输入（导航指令、自车状态）与输出（轨迹、3D 位置）全部表示为自然语言文本，最大化利用 Gemini 的世界知识。
- **链式思维推理 (Chain-of-Thought)**：使用 CoT 推理增强决策，端到端规划性能提升 6.7%，并提供可解释的驾驶决策理由。
- **多任务协同训练 (Co-training)**：联合训练规划轨迹预测、目标检测和道路图理解带来正向任务迁移，单个协同训练的 EMMA 能同时产出多任务输出，性能匹配甚至超越单独训练的模型。

## 评测

- 在 nuScenes 运动规划上达到 SOTA。
- 在 Waymo Open Motion Dataset (WOMD) 上取得有竞争力的结果。
- 在 Waymo Open Dataset (WOD) 上以摄像头为主的 3D 目标检测取得有竞争力结果。

## 局限

- 当前对长时视频序列处理能力有限，限制其对实时驾驶场景的推理。
- 未利用 LiDAR 与雷达输入，需要更复杂的 3D 感知编码器融合。
- 需要高效的仿真评估方法、优化推理时间、验证中间决策步骤。

## 定位

EMMA 是 Waymo 的研究成果，展示了多模态大模型用于自动驾驶的潜力，属于内部研究模型，未作为独立量产驾驶系统对外提供。
