# Scaling GAIA-1: 9-billion parameter generative world model for autonomous driving (blog)

Source: https://wayve.ai/thinking/scaling-gaia-1/
Fetched: 2026-08-27
Date: 3 October 2023 | Research

In June 2023, Wayve unveiled GAIA-1 as the first proof of concept of a cutting-edge generative model for autonomous driving. GAIA-1 was optimised to generate videos at higher resolution and improve the world model's quality with larger-scale training. This blog releases the technical report and results of scaling GAIA-1 to over 9 billion parameters.

Overview: GAIA-1 is a generative world model built for autonomous driving. A world model learns representations of the environment and its future dynamics. GAIA-1 leverages video, text and action inputs to generate realistic driving videos and offers fine-grained control over ego-vehicle behaviour and scene features. Due to its multi-modal nature, GAIA-1 can generate videos from many prompt modalities and combinations.

Prompts: GAIA-1 can generate videos by performing future rollout starting from a video prompt. Rollouts can be conditioned on actions (e.g. steer left), or text (e.g. change the colour of the traffic light). For speed and curvature, GAIA-1 is conditioned by passing the sequence of future speed and/or curvature values. GAIA-1 can also generate videos from text prompts, or by drawing samples from its prior distribution (fully unconditional generation).

Model architecture and training:
- GAIA-1 encodes all inputs through specialised encoders for each modality (video, text, and action) projecting them into a shared representation. These encoded representations are temporally aligned.
- The core component, the world model, is an autoregressive transformer that predicts the next set of image tokens in the sequence, considering past image tokens and contextual text and action tokens.
- GAIA-1's world model has 6.5 billion parameters and was trained for 15 days on 64 NVIDIA A100s.
- Finally, the video decoder, a video diffusion model, translates predicted image tokens back into pixel space, ensuring generated videos are semantically meaningful, visually accurate, and temporally consistent.

Total model scale: over 9 billion parameters. arXiv technical report released.
