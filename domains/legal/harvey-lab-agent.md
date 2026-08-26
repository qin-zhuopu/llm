---
title: "Training a State-of-the-Art Legal Agent with Harvey"
date: JUNE 22, 2026
source: "https://appliedcompute.com/case-studies/harvey"
---

We collaborated with Harvey to post-train a frontier legal model on top of GLM-5.1. In [Harvey's Legal Agent Benchmark⌝](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (LAB), our trained model outperformed every available model on rubric pass rate. Notably, we found that it outperforms Opus 4.8 Max and GPT-5.5 xhigh, a threshold that previous trained models across the industry had not yet reached.
Rubric pass rateAll pass eval score
GLM-5.1 improves from 0.853 to 0.913 rubric pass rate, exceeding both GPT-5.5 xhigh and Opus 4.8 Max. For all evals, we repeated grading 3 times and reported the average to account for grader variance.
We optimized the end-to-end training process, spanning data and grader analysis, harness engineering, and full-parameter reinforcement learning. All reported eval scores are on a held-out test split that mirrors the full LAB distribution.
## Why Legal Work is a Demanding Test
Legal work is challenging for AI agents because partial success is often not enough. A response can be fluent, plausible, and mostly correct, yet still fail if it misses a required clause, overlooks a document, misstates a jurisdictional detail, or fails to satisfy one part of a multi-step instruction.
Harvey's open-source Legal Agent Benchmark (LAB) is designed around that standard. It is difficult not only because the tasks are complex, but also because the grading schema is strict: a task passes only when all of its required criteria are satisfied.
LAB contains more than 1,250 tasks across 24 legal practice areas. Each datapoint includes source documents, task instructions, and a task-specific rubric. In total, the benchmark contains more than 75,000 binary criteria. This makes LAB difficult for frontier models, since performance depends not only on broad legal reasoning, but also on sustained attention, tool use, document handling, and consistency across every part of a task.
## Methodology with AC2
Training a frontier model on tasks as difficult to verify as LAB requires trust in the optimization signal. A powerful open-weight model will learn to exploit any flaw in the grader via loopholes in the evaluation criteria and environment. We conducted evaluations, training jobs, consistency checks, and the supporting analysis on our platform [Applied Compute Agent Cloud⌝](https://www.appliedcompute.com/#platform).
We present evaluations of closed and open-weight models describing the frontier of performance on LAB tasks. All evaluations (except baselines for harness comparisons) are run with the same final compaction harness and max reasoning effort. Evaluations use GPT-5 Mini as the grader model with batches of 4 criteria-per-call.
## Data Analysis
We conducted a thorough analysis over data and graders to determine the best setup for training.
### Grader Alignment
Since LAB utilizes LLM-as-a-Judge for its grading methodology, we analyzed a set of frontier models to determine the best judges for the task. We pulled the two strongest frontier models available at the time of analysis (GPT-5.5 and Opus 4.7) and ran a 50-point subset through the original LAB harness, producing traces covered by over 2,500 rubric criteria. We then reran candidate grader models three times each to measure self- and cross-consistency.
GPT-5.5 xhigh and Claude Opus 4.7 Max agreed on over 95% of criteria across all runs. We treat this consensus set as the gold-trace ground truth and use it to evaluate the candidate graders: GPT-5.5, Claude Opus 4.7, GPT-5 Mini, Claude Sonnet 4.6, GPT-5 Nano, and Claude Haiku 4.5. We found that medium-sized models such as GPT-5 Mini and Claude Sonnet 4.6 largely maintained quality, staying above 97% alignment with the agreed-upon frontier ground truth. Among the smaller models, performance varied: GPT-5 Nano remained near the mark at 95%, while Haiku 4.5 fell more substantially to 82%. GPT-5.5, Claude Opus 4.7, GPT-5 Mini, and Claude Sonnet 4.6 were highly self-consistent; across three reruns. We found a floor of 98.9% per-criteria self-consistency, showing the LAB set to be well-constructed with few ambiguous or flaky criteria. Alignment for these top four graders is further supported by cross-consistency metrics like a 0.99 Pearson correlation across criteria.
### Cost-alignment Pareto Frontier
Given the high alignment and consistency found with graders of a medium size class, we examined exchanging quality for cost compared to the largest and most expensive models. We sought to understand the performance tradeoff of two changes from the original LAB setup: switching to smaller grader models, and grouping multiple criteria into each grader call instead of evaluating one criterion per call. Below, we measure alignment on the y-axis and a log-scale of mean-cost-per-trace, all relative to the original LAB setup with 1 criteria per grader call to Claude Sonnet 4.6. By switching to GPT-5 Mini and batching multiple criteria per-call, we observed between 40x (at 16-per-group) and 100x (at all-criteria-in-one-group) cost savings relative to the original setup. This finding enabled us to scale up grading and sampling for high-compute RL runs.
Cost reductions relative to claude-sonnet-4-6 with 1 criteria-per-call baseline. Both grader candidates are measured against frontier model agreement to GPT-5.5 xhigh and Opus 4.8 Max. Annotations represent the number of criteria-per-call, showing how batching groups of criteria can lead to massive cost savings. Note the x-axis mean cost per trace log scale.
## Harness Improvements
We began with the harness published by Harvey in the LAB repository, which includes simple tools like read and grep over files mounted into a sandboxed execution environment. We worked to closely match the reported scores from the Initial Results on Legal Agent Benchmark blogpost. Once we confirmed parity with the original harness, we utilized the AC2 platform to find simple, scalable improvements on the way to a strong, generalizable legal agent harness. For example, restricting the number of tokens in tool output, repairing broken tool calls, providing advice on tool-use, and adding reminders to produce outputs led to large improvements for open-weight and closed source models. After hill climbing by adjusting the harness, we added a compaction function to allow the model to work for longer on this task.
Eval score by harnessAll pass eval score
Comparison of baseline LAB harness to final AC harness with compaction, better prompts, stronger tool descriptions, and reminders. All evals are run against GPT-5 Mini with 4 criteria-per-group. All evaluations run against base checkpoints or APIs.
The baseline evaluation is as close as possible to the original LAB harness. For the baseline comparison, all models are run against their native context length. Harness hillclimbing was done against many candidate base models to drive improvements across model family and scale. Notably, while almost all models largely benefit from the jump from the base harness to the AC harness, our chosen base model for training GLM-5.1 stayed roughly the same after the harness update and only improved when it was trained to better utilize tools and address its own failure cases.
### Compaction
A small fraction of rollouts (around 10% with the base GLM-5.1 model) reach the max context length limit due to the abundance of large files which the agent pulls into context. In the LAB dataset, the 90th-percentile datapoint contains nearly 100,000 tokens in source documents with the maximum rising to over 200,000 tokens of source documents. We incorporated compaction into our harness by automatically triggering compaction to summarize the current conversation when it reached a certain token limit. Compaction involves the harness sending the current episode's transcript to the same agent for summarization (using the same weights, but a different system prompt). Then, a fresh conversation starts from that summary. For the final compaction harness, we use a compaction trigger of context_tokens >= 131072 and up to 4 max_compactions.
In conjunction with the analysis work above, we set out to train the best possible model with full-parameter fully-asynchronous RL on AC2. We conducted derisking runs with Qwen 3.6 35B A3B and Kimi K2.6 to determine the strongest harness and hyperparameters, and we ultimately settled on training GLM-5.1 due to its superior performance on the baseline.
## Training
Before training, GLM-5.1 starts well below the frontier of GPT-5.5 xhigh and Opus 4.8 Max; over the course of training, our model exceeds Opus 4.8 Max and GPT-5.5 xhigh on the dense rubric passrate eval score and approaches Opus 4.8 Max on the all-pass eval score. We attribute the capabilities gains on the model mostly to improved tool call usage and reasoning about the source documents.
Rubric pass rateAll pass eval score
Training curves showing rubric pass rate (left) and all-pass eval score (right) over training steps. The model progressively exceeds GPT-5.5 xhigh and approaches Opus 4.8 Max.
## Model Analysis
We analyzed the way the model changes over the course of training using the AC2 platform. We see the train and eval scores increase from the beginning to the end of training, but what learnings and advancements are actually driving those improvements in scores?
### Distribution Analysis
We can utilize the LAB datapoint subdomains in order to see which sectors see the most improvement. antitrust-competition improves the most, followed by intellectual-property and energy-natural-resources. A few domains see minor regressions, with structured-finance-securitization seeing a small loss. The regressing domains have the smallest share in the train and test sets.
Domain-Level Beginning-to-Final Score Shift. Score difference between trained and baseline model across 24 legal practice areas.
### Tool-Use Analysis
Over the course of training, we see total tool usage fall; this breaks down mostly into fewer read calls with a consistent number of other tool calls, like bash and grep. As the eval score continues to improve, this reflects the model learning to more effectively use its tools and not just bulk-read all the files in the source documents. Likewise, the model sets more limits and uses the read tool more specifically, which reduces the total payload tokens per trace over the course of training.
Tool calls per traceTool payload tokens
Left: Total tool calls (and breakdown by type) per eval trace over training steps. Right: Tool payload tokens per trace over training steps. Both metrics decrease as the model learns more targeted tool use.
### Behavior Analysis
Beyond explicit behaviors like tool use, we were interested in the qualitative changes in the model's behavior. Since the model baseline score starts around 85%, only approximately 1,500 rubric criteria remain to be improved across the 180-item test set (with roughly 10,000 total criteria). We saw three specific behaviors that improve over training and lead directly to higher scores.
  1. **Artifact Completeness** : The model learned to properly use tools and always create an output artifact. This behavior flipped 185 relevant rubric criteria from failing to passing during the course of training.
  2. **Specificity and Exactness** : The base GLM-5.1 model suffers from poor calculations or referring to imprecise numbers, often rounding figures during math (like 1.9 to 2), which is punished by legal graders. This behavior flips 243 criteria from failing to passing.
  3. **Grounding** : Without training, the checkpoint sometimes hallucinates source document items or invents findings from outside the provided documents. Despite not training against an explicit hallucination penalty, we see this behavior drop over time. This behavior flips 70 criteria from failing to passing during training.

These three behaviors accounted for part of the model's improvement from the first step to the last. Many criteria flipped from failing to passing, but some criteria tied to these same behaviors still fail in the final checkpoint, which suggests the model has not yet reached its performance ceiling.
### Example Rollouts
We can directly observe these learned behaviors by comparing traces from held-out eval points at the beginning and end of training. Below, we compare attempts to solve a LAB task from the untrained base GLM-5.1 model and our final trained checkpoint. In this task, the assignment is to review a set of documents for a proposed acquisition for Prism and produce a memo describing transaction structure, risk areas, and recommended next steps backed by specific details from the source documents.
Metric| GLM-5.1 Base| AC GLM-5.1  
---|---|---  
Rubric Score| .061| .803  
Turns| 40| 16  
Tool calls| 104| 42  
Read calls| 44| 24  
Bash calls| 44| 16  
Tool payload tokens| 461k| 250k  
Over the course of training, the trained checkpoint exhibits markedly fewer total tool calls and makes more precise, targeted use of its bash and read calls. This results in vastly smaller total payloads returned from tools. Due to our compaction harness, the model can ingest far more tokens than its max context length but must learn to effectively use that effective context and avoid context rot.
In the base checkpoint, we see many uses of calls to functions ls, echo, and cat via the bash tool that dump huge amounts of tokens into the context window. Once the model attempts to make an output deliverable, it wastes 16 tool calls creating and revising its deliverable. In contrast, the trained model avoids unhelpful tool calls and uses targeted reads to collect context and relies on only two tool calls to construct and then verify its final deliverable.
In this task, the assignment is to review a set of documents for a proposed acquisition for Prism and produce a memo describing transaction structure, risk areas, and recommended next steps backed by specific details from the source documents. We see markedly better specificity and grounding in these trace excerpts:
### GLM-5.1 Base
### AC GLM-5.1
Tool Use Examples  
---  
  1. read documents/market-data-summary.xlsx returned over 200,000 characters into the token stream.
  2. Builds a custom docx Python script that ultimately fails to construct an artifact due to a parsing error — instead of using the available docx generation tool.
  3. Failure to check the correct location (/workspace/outputs) for the output artifact, resulting in 'No such file or directory' and lack of verification of the docx file type.

  
Tool Use Examples  
---  
  1. read documents/kinney-pricing-email.eml offset 0 limit 1000 returns specified context "On Mon, Aug 12, 2024 at 3:47 PM Robert Kinney...".
  2. bash grep "commercial payors" documents/*.eml highlighted the exact necessary phrase from a source email.
  3. bash generate_from_md.py memo.md output/pre-notification-briefing-paper.docx — correctly structured to use the provided tool and deliver a docx file type, followed by properly using the verify tool for a successful submission.

  
Final Deliverable Excerpts  
---  
  1. "the Pinnacle/Meridian Transaction, a contemporaneous acquisition...rate increases from BlueCross BlueShield" shows a focus on the wrong acquisitions due to overly broad file reads.
  2. Generalizations like "post-merger pricing power will increase" lead to poor grader scores due to lack of specificity.
  3. Poorly supported claims like "Vertical concerns arise from ClearScript PBM, LLC, Meridian's wholly-owned pharmacy benefits management subsidiary..." lack evidence.

  
Final Deliverable Excerpts  
---  
  1. References the correct source documents and specific dates: "in the Kinney-Thornbury Pricing Email (August 12, 2024)".
  2. "Exclusive Hospital Outreach Contracts (Total: $76M annual revenue, 30.8% of Prism revenue)" details specific, grounded information relevant to the deliverable.
  3. Grounded references to specific details "Prism Diagnostics purchases approximately $620,000 in AllerSpec proprietary allergy reagent kits annually from LabVantage's Cascade Reference Labs subsidiary..." further the legal argument.

  
These trace excerpts show the model's learned behaviors, showcasing its ability to make efficient, effective tool calls and make specific, grounded claims with relevant context from the supporting source documents.
## Conclusion
Through our collaboration with Harvey on LAB, we trained GLM-5.1 into a state-of-the-art legal agent by optimizing the full stack: grader, harness, and full-parameter reinforcement learning on AC2. The resulting model lifts rubric pass rate from 0.853 to 0.913 and all-pass rate from 0.059 to 0.126, making it the strongest available model by rubric pass rate and second only to Opus 4.8 Max on all-pass rate.
Just as importantly, our analysis traced these gains to concrete, interpretable behaviors in improved artifact completeness, sharper specificity, and stronger grounding, showing that the improvements reflect real legal competence.
We're grateful to the Harvey team for their partnership, their open LAB benchmark, and their deep domain expertise throughout this effort. With our better understanding of the remaining headroom, we believe complementary techniques can continue improving the model. We expect further gains from relevance-masked self-distillation to strengthen grounding and agentic router training to optimize for cost alongside quality. We look forward to continuing to push the frontier of vertical agents with Harvey and sharing more as these systems move from benchmarks into production.
ABOUT THE COMPANY
Harvey builds AI solutions for the legal industry, helping law firms and legal teams work faster and smarter. Their open-source Legal Agent Benchmark (LAB) sets the standard for evaluating AI agents on complex legal tasks.
[Visit Site ⌝](https://harvey.ai)
INDUSTRY
Law
CHAMPIONS
Gabe Pereyra
Niko Grupen
SHARE