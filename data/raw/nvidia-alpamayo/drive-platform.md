# NVIDIA DRIVE / Alpamayo (developer page)

Source: https://developer.nvidia.com/drive
Fetched: 2026-08-27

NVIDIA provides an end-to-end stack for autonomous vehicle development — from sensor data curation and synthetic data generation to model training, closed-loop simulation, and production-grade in-vehicle compute.

Fine-Tune a Reasoning Foundation Model on Fleet Data:
NVIDIA Alpamayo 2 Super is an open 34B VLA (vision-language-action) reasoning foundation model with RL post-training, flexible multi-camera support, and navigation guidance. Post-training scripts for SFT and RL fine-tuning on proprietary fleet data are available on GitHub under Apache 2.0.

NVIDIA AlpaGym: the first modular RL framework for training AV policy models at GPU scale, running models through continuous decision and observation cycles to expose compounding errors that static datasets miss.

NVIDIA AlpaSim: an open-source closed-loop AV simulation framework with a microservice architecture assigning rendering, physics, traffic behavior, and policy execution to separate GPU resources.

Related NVIDIA AV components:
- DRIVE AGX (Orin, Thor) automotive-grade in-vehicle compute; DriveOS SDK with DriveWorks, CUDA, TensorRT.
- Cosmos Curator / Cosmos Reason VLM for multimodal data curation.
- CoC Auto-Labeling Pipeline: automatically generates Chain of Causation reasoning labels for driving clips.
- Omniverse NuRec: Gaussian-based reconstruction of real-world driving data into interactive simulation.
- Cosmos Transfer: world foundation model generating photorealistic synthetic driving data from HD Maps, lidar depth, and text prompts.
