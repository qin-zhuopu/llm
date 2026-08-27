# Introducing Waymo's EMMA — End-to-End Multimodal Model for Autonomous Driving (blog)

Source: https://waymo.com/blog/2024/10/introducing-emma
Fetched: 2026-08-27

EMMA (End-to-End Multimodal Model for Autonomous Driving) is powered by Gemini, a multimodal large language model developed by Google. EMMA employs a unified, end-to-end trained model to generate future trajectories for autonomous vehicles directly from sensor data. Trained and fine-tuned specifically for autonomous driving, EMMA leverages Gemini's extensive world knowledge to understand complex scenarios on the road.

EMMA demonstrates positive task transfer across several key autonomous driving tasks: training it jointly on planner trajectory prediction, object detection, and road graph understanding leads to improved performance compared to training individual models for each task.

Key aspects:
- End-to-End Learning: EMMA processes raw camera inputs and textual data to generate driving outputs including planner trajectories, perception objects, and road graph elements.
- Unified Language Space: EMMA represents non-sensor inputs and outputs as natural language text to maximize Gemini's world knowledge.
- Chain-of-Thought Reasoning: EMMA uses chain-of-thought reasoning, improving end-to-end planning performance by 6.7% and providing interpretable rationale for its driving decisions.

EMMA achieves state-of-the-art or competitive results on multiple autonomous driving tasks on public and internal benchmarks, including end-to-end planning trajectory prediction, camera-primary 3D object detection, road graph estimation, and scene understanding. A single co-trained EMMA can jointly produce outputs for multiple tasks while matching or surpassing individually trained models.

Limitations: current limitations in processing long-term video sequences; does not leverage LiDAR and radar inputs; needs efficient simulation for evaluation; optimized inference time; verification of intermediate decision-making steps.

"EMMA is research that demonstrates the power and relevance of multimodal models for autonomous driving." — Drago Anguelov, Waymo VP and Head of Research
