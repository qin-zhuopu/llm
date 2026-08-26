---
title: "Post-Training Collaboration with NVIDIA"
date: AUGUST 5, 2026
source: "https://appliedcompute.com/case-studies/nvidia"
---

Applied Compute deploys custom [Nemotron models⌝](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/) in production for our frontier enterprise customers in software engineering, financial services, logistics, and AI-native companies.
We are collaborating on multiple projects that are in service of better open-source models and systems around those models.
### **De-risking mainline RL runs**
  * For a targeted capability, Applied Compute runs the RL training end to end on our own stack.
  * We then share the research results with NVIDIA from the capability ceiling reached on that task distribution, the shape and slope of the training curve, which reward designs hold up and which get hacked, and the recipe configuration behind the result.

The [Applied Compute Agent Cloud⌝](https://www.appliedcompute.com/#platform), AC2, enables the full iteration cycle across evals, data curation, training experiments, and inference in a single platform. This surfaces instability, reward hacking, and recipe problems early, when they still cost a fraction of what they would at full scale.
### **Production workload statistics**
Production workload statistics. Applied Compute runs a large, varied production footprint and shares statistics from it such as number of turns and number of output tokens per turn.
Our [public inference benchmark⌝](https://www.appliedcompute.com/research/inference-benchmark) is a preview of this work: production agentic workload proﬁles (agentic coding, code QA, and oﬃce work) drawn from multi-turn deployments and released with an open-source harness for replaying them against inference engines. The profiles come from recorded traces, not fixed input and output lengths. Agentic coding averages about 20 tool turns per trace, with office work averaging 41 turns, and code QA running as high as 200, with 200 to 300 assistant tokens per turn against prompts that start near 10k and grow with every tool result. Replaying them on DeepSeek R1, vLLM and SGLang track each other closely but both lose throughput as concurrency rises, because KV evictions drag the eligible cache hit rate down.
### **An Ongoing Initiative**
Applied Compute runs Nemotron across multiple frontier-enterprise deployments today, and our post-training and inference platform AC2 is built for the multi-turn, agentic workloads Nemotron targets.
As each new Nemotron version ships to customers, this loop is what makes it better, proven on the real workloads people run in production rather than on benchmarks alone.
ABOUT THE COMPANY
NVIDIA designs GPUs and the CUDA software stack used for AI training and inference. Nemotron is its family of open models.
[Visit Site ⌝](https://www.nvidia.com/en-us/)
INDUSTRY
Technology
SHARE