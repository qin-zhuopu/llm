# Physical Intelligence (π) — Robotic Foundation Models (π0 / π0.5 / π*0.6 / π0.7)

Source: https://physicalintelligence.company/ and https://www.physicalintelligence.company/blog/pi0 (fetched 2026-08-27)

Physical Intelligence (π) is bringing general-purpose AI into the physical world. It develops learning algorithms and robotic foundation models designed to control any robot to do any task — directly relevant to manufacturing automation, assembly, material handling, and factory robotics.

## Model line
- π0 (Oct 2024): first generalist policy — a vision-language-action (VLA) flow-based model combining large-scale multi-task and multi-robot data collection with a new network architecture. Open-sourced (weights + code) in Feb 2025, along with π0-FAST autoregressive variant.
- π0.5 (Apr 2025): extends π0 with open-world generalization; can control a mobile manipulator to clean an entirely new kitchen or bedroom.
- π*0.6 (Nov 2025): a VLA that learns from experience, trained with RL to improve success rate and throughput on real-world tasks.
- π0.7 (Apr 2026): a steerable model with emergent capabilities, showing a step-change in generalization.

## Technical (π0, from public paper arXiv:2410.24164)
- Architecture: vision-language-action (VLA) model built on top of a pretrained vision-language model (PaliGemma, ~3B) with an added action expert; ~3.3B total parameters.
- Uses flow matching (a variant of diffusion) to represent continuous action distributions, enabling high-frequency dexterous control (up to 50 Hz).
- Trained on a large cross-embodiment dataset spanning 7+ robot configurations and 68 tasks, plus the Open X-Embodiment dataset.
- Action chunking + real-time inference for smooth manipulation.
- π*0.6 adds reinforcement learning from real-world experience ("Recap" method) to improve throughput/success.

## Research topics
- Multi-Scale Embodied Memory (MEM): long- and short-term memory for tasks longer than ten minutes.
- Real-Time Action Chunking (RTC) for large VLAs under high latency.
- Human-to-robot transfer in VLAs; RL Token extraction for fast online RL.

## Business
- Founded 2024; raised ~$400M at a ~$2.4B valuation, then reportedly ~$600M+ at higher valuations.
- Backers: Bond, Jeff Bezos, Khosla Ventures, Lux Capital, OpenAI, Redpoint Ventures, Sequoia Capital, CapitalG, Thrive Capital.
- Follow at @physical_int.
