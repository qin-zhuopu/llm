# Microsoft MatterGen

> 来源: [https://www.microsoft.com/en-us/research/blog/mattergen-a-generative-model-for-inorganic-materials-design/](https://www.microsoft.com/en-us/research/blog/mattergen-a-generative-model-for-inorganic-materials-design/)
> 抓取时间: 2025-06-17
> 公司: Microsoft

---

## MatterGen: A Generative Model for Inorganic Materials Design

MatterGen is a generative AI model developed by Microsoft Research in collaboration with the Azure Quantum team, designed for inorganic materials discovery. Published in Nature (2024), it represents a paradigm shift from traditional high-throughput screening to guided generation of novel materials with desired properties.

### Core Technology

MatterGen uses diffusion models - the same class of AI models used for image and video generation - adapted for materials science. Instead of generating materials at random and then screening them, MatterGen generates materials in a focused way that have specific values of:
- Magnetic density
- Bandgap
- Other desired physical properties

This approach provides several orders of magnitude acceleration over traditional random screening methods in exploring the vast combinatorial space of possible new materials.

### Architecture and Approach

The model leverages key principles from AI for science:
- **Inductive biases from physics**: Incorporates symmetries (invariance and equivariance properties) that encode known physical laws
- **Emulator approach**: Uses density functional theory (DFT) simulations to generate synthetic training data, then trains deep learning emulators that are 3+ orders of magnitude faster than the original simulators
- **Diffusion-based generation**: Generates crystal structures by iteratively denoising from random configurations to stable material structures with targeted properties

### Key Results and Applications

**Lithium-ion Battery Electrolytes:**
- Screened over 32 million computer-generated candidate materials
- Reduced a multi-year computation process to just 80 hours
- Discovered a new battery electrolyte material that uses 70% less lithium than standard lithium-ion batteries
- Material was synthesized and experimentally validated at Pacific Northwest National Laboratory
- Test batteries were fabricated and demonstrated to power devices

**Materials Generation:**
- Can generate materials conditioned on specific property targets
- Achieves focused exploration of subspaces within the vast combinatorial materials space
- Combines with accelerated AI screening for multiplicative speedups

### Integration with Azure Quantum

MatterGen is part of Microsoft's broader Azure Quantum Elements platform, which provides:
- Cloud-based quantum chemistry simulations
- AI-accelerated materials discovery workflows
- Integration with experimental validation pipelines

### Scientific Foundation

The model builds on fundamental principles:
- No-free-lunch theorem: compensating for scarce scientific data with powerful inductive biases from 350+ years of physics
- Schrödinger's equation approximations via DFT for training data generation
- Geometric deep learning respecting molecular symmetries (rotational invariance/equivariance)
- Conservation laws (momentum, energy, charge) embedded in model architecture

### Publication

Published in Nature (2024), demonstrating experimental validation of generated materials. The work represents a collaboration between Microsoft Research and the Azure Quantum team.

---

> 补充来源: [MatterGen: a generative model for inorganic materials design (arXiv 2312.03687)](https://arxiv.org/abs/2312.03687)
> 抓取时间: 2026-08-30

## arXiv 预印本（同行评审论文）

MatterGen 的技术论文 arXiv:2312.03687（后正式发表于 Nature 2025，DOI 10.1038/s41586-025-08628-5）由 Tian Xie 等微软研究院团队撰写。论文提出基于扩散的生成过程，通过逐步细化原子类型、坐标与周期晶格来产生晶体结构，并引入 adapter 模块支持面向任意性质约束的微调。相较此前生成模型，MatterGen 产生的结构新颖且稳定的概率高出 2 倍以上，距局部能量最小值近 15 倍。微调后可生成满足指定化学组成、对称性以及力学/电子/磁学性质的稳定新材料，并展示了兼顾高磁密度与低供应链风险组成的多性质设计能力。
