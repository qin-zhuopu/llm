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
