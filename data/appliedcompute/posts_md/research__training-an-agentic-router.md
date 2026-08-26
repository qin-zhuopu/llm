---
title: "Training an Agentic Router for Optimal Cost-Performance on SWE Tasks"
date: JUNE 4, 2026
authors: "NIC BECKER, RHYTHM GARG"
source: "https://appliedcompute.com/research/training-an-agentic-router"
---

On most enterprise tasks, model quality is not a scalar. One model is better at long-horizon repository exploration. Another is better at small, surgical patches. A third has stronger general reasoning but higher latency or cost. The right model depends on the task, the environment, and the failure mode that matters.
This is especially apparent in agentic software engineering, where every task unfolds as a trajectory. The model reads files, searches the repository, forms a hypothesis, edits code, runs tests, and decides when to stop. The best model for one issue may be the wrong model for the next one.
Routing each task to the model best suited to solve it captures the strengths of specialized models and routes around their weaknesses, instead of settling for one model's compromises across the board. But this only works with a router that picks the model most likely to solve a given task, at the lowest cost, using the local evidence available before the rollout begins.
Many of our workloads at Applied Compute involve software engineering, so we trained a small open-source model (Qwen3.6-35B-A3B) to route SWE-bench Verified tasks across three frontier coding models: [Nemotron 3 Ultra⌝](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/#nemotron-3-ultra) (which we received early access to), GPT-5.5, and Claude Opus 4.7. The router sees the issue and repository context, predicts which model should attempt the patch, and is trained against labels derived from actual agent rollouts.
### **Task Distribution**
We used SWE-bench Verified as the task distribution. For each task, we collected three rollouts from each candidate model:
  * Nemotron 3 Ultra
  * Claude Opus 4.7
  * GPT-5.5

Each rollout attempted to produce a patch for the repository issue. We then evaluated whether the patch passed the task’s tests. This gave us task-level evidence about which models could solve which problems, and at what cost.
The router was then trained on the routing decision. Crucially, we excluded patch generation from the training data because the router does not need to know how to fix the bug itself.
This distinction matters. It means that a small router can be trained cheaply and deployed in front of much larger models. The router can inspect the issue, repository metadata, and derived features, then choose the model whose rollout is expected to give the best cost-quality tradeoff.
### **Oracle Routing Labels**
We started with a simple label construction. For each task, we identified the model with the strongest observed outcome. If multiple models tied on performance, we chose the cheapest model among the tied models, using average rollout cost as the tie-breaker. We called this the winning model for the task.
The router got a reward of 1 if it chose the winning model, and 0 otherwise.
There are more nuanced reward functions that we plan to explore in future work: soft labels, margin-aware rewards, expected utility, calibrated pass probability, or penalties for routing to unnecessarily expensive models. But binary oracle imitation gave us a high-signal training run and an interpretable baseline.
### **The Routing Ceiling**
Before training the router, we computed an oracle ceiling: the performance of a policy that always routes each task to the best observed model, breaking ties by cost. This is the upper bound on what any router could recover from our rollout data, and it tells us how much headroom exists over always using a single model.
**Cost Optimization Matters**
For agentic systems, cost is not an implementation detail; it determines what can be deployed at all. A model that is slightly more accurate but far more expensive can be the wrong default, while a cheaper model that solves a large share of the task distribution is valuable even when it is not the best on every task. So when two models reach the same pass rate on a task, the oracle credits the cheaper one.
**The Results**
On 497 SWE-bench Verified tasks, the oracle policy routes most tasks to Nemotron 3 Ultra, with smaller but meaningful slices going to Claude Opus 4.7 and GPT-5.5.
This already tells us that the models are not redundant. Even when one model is strong on average, there are still tasks where another model is the better production choice.
The same pattern appears in pass rate. Always using a single model leaves performance on the table. The oracle policy improves the aggregate pass rate by selecting the best model per task.
In the current rollout set, the single-model baselines are:
Policy|  Mean avg@k pass score  
---|---  
Always Claude Opus 4.7| 0.834  
Always Nemotron 3 Ultra| 0.710  
Always GPT-5.5| 0.776  
Oracle routing label| 0.890  
The oracle ceiling is not a deployable policy, since it picks the best model for each task by looking at the answer key. But it shows the upside. If a trained router can learn enough of that pattern from the task context alone, the deployed system can beat the best single model.
### **What the Router Sees**
The router is trained to make a decision before the expensive model rollout begins. The router's input is the task description, the repository context, and a high-level capability analysis of the candidate models, derived only from the training set.
**How the seed policy is constructed: cost-aware capability analysis**
We isolate a discriminative subset of tasks where there is a non-zero gap between the best and worst model's avg@3 score, and split it three ways by which model uniquely won. For each slice, we use a read-only agent to conduct a per-model analysis pass. The agent reads a sample of representative tasks, plus a small sample of full rollout transcripts, and identifies recurring problem-solving strategies that benchmark accuracy alone doesn’t capture.
A synthesis pass then keeps only the patterns that:
  * generalize to high-level guidance,
  * replicate across multiple repositories,
  * are router-observable, meaning they do not depend on the test patch or any other field the router cannot see at routing time,
  * clear a calibrated effect-size bar (at least 15 percentage points above the marginal best-model rate, with a sample size large enough to support a Wilson confidence interval), and
  * pass a cost-adjusted bar: routing to a more expensive arm earns a rule only if its observed accuracy lift over the cheapest competitive model is large enough to justify the per-task cost premium.
  * Ties at the top of the per-task pass-rate distribution resolve in favor of the cheaper model.

That last criterion is what makes the seed policy lean on Nemotron 3 Ultra as the default. On task shapes where Nemotron is at or near the panel-best pass rate, the cost discount over the closed-API arms is decisive: routing to Opus or GPT would pay a real premium for noise-scale accuracy gains.
Patterns that survive become the capability analysis the router sees. Patterns that don't, including patterns that _would_ favour a more expensive arm if cost were ignored, are recorded as anti-signals in the prompt, explicit "this looks like it should matter, but it doesn't" cues so the router doesn't reach for them intuitively.
Observed pattern| Model advantage|  Router implication| Evidence  
---|---|---|---  
Narrow, well-localised bug reports; a clearly named symbol, expected behavior stated in one or two sentences, and a fix that plausibly lives at one site.| Nemotron 3 Ultra| **Default.** Use unless another rule below fires.| 19 of 24 tasks where Nemotron uniquely outperformed the panel fit this shape. Across the broader competitive-Nemotron population, the per-task Opus-over-Nemotron pass-rate delta does not exceed the Opus cost premium, so the cost-adjusted bar pins the default to Nemotron. Opus's failure mode on the same shape is over-engagement with the test scaffolding: inventing tests, colliding with the gold test patch, second-guessing a correct fix when a stale test contradicts it.  
Python language-spec and protocol semantics; dunder methods, MRO, metaclass interactions, the descriptor / attribute-lookup protocol, NotImplemented-as-return-value, deprecation cycles, etc. The patch is small, but the correctness argument lives in the language spec.| Claude Opus 4.7| **Route to Opus.**|  Strongest qualitative signal in the Opus-best slice; pattern recurs across at least six repositories, so the rule isn't a single-repo prior in disguise. On this slice the per-task Opus-over-Nemotron pass-rate delta exceeds the per-task Opus cost premium.  
Cross-cutting API consistency complaints — phrasings like "is inconsistent with X" / "should match Y" / "X does this but Y doesn't" — combined with evidence that the symbol named in the complaint is referenced from more than two source files in the package.| Claude Opus 4.7| **Route to Opus when the symbol-spread check fires** (e.g. grep -rln <symbol> returns more than two source files). The bash gate is what makes the rule router-observable; the underlying "patch touches multiple files" signal is oracle-only.| Recurring theme in the Opus-best slice; this is the multi-file-fix tail where the Opus-over-Nemotron pass-rate delta is the widest in the table and clearly exceeds the Opus cost premium. Without the bash gate the rule mis-fires on single-site inconsistencies, where Nemotron is competitive and the cost-adjusted bar swings back to the default.  
Parser or recogniser fixes that have to track an external spec — the user points to a PEP, language standard, or sibling tool that defines the valid form, and the fix is a small grammar or normalisation change that has to match it.| Claude Opus 4.7| **Route to Opus.**|  Third recurring Opus theme. The patch is usually small, but it has to track a spec the cheaper default does not internalise reliably. On this slice the per-task Opus-over-Nemotron pass-rate delta exceeds the per-task Opus cost premium.  
Several plausible-sounding signals were tested and dropped. In every case because either the raw accuracy signal failed or the cost-adjusted bar failed:
  * **Stack trace in the problem statement.** Present on roughly equal shares of Opus-best, Nemotron-best, GPT-best, and tied tasks. Adding it as either a positive or negative rule is unsupported on accuracy alone, before cost is even applied.
  * **Long problem statements.** The Opus-best problem-statement length distribution is actually _below_ the full-set median, not above. The longer-PS slice does concentrate GPT-best tasks, but it bleeds heavily into Opus-tied tasks where the routing would pay the GPT cost premium for zero accuracy lift.
  * **Documentation, build-tool, and extension-machinery internals.** The models tend to perform similarly in the panel.
  * **A positive GPT-5.5 routing rule.** GPT-5.5 is the strict best on only 22 of 497 tasks, and 18 of those win by a single rollout, inside avg@3 sampling noise. The four substantial-margin tasks span unrelated repos and patch shapes, with no router-observable signal that picks them out without dragging in a much larger false-positive slice. The seed policy treats GPT-5.5 as an "only when there's a clear edge over Opus" fallback rather than the target of a rule.

The result is a router that knows more than which model is strongest. It knows where strength is worth paying for, where the cheap default already wins, and which intuitive signals to leave alone.
### **Training**
We trained a Qwen3.6-35B-A3B router.
The router outputs one of three actions:
  * Route to Nemotron 3 Ultra
  * Route to Claude Opus 4.7
  * Route to GPT-5.5

We ran several ablations to find the best configuration for a router that stably improves and avoids collapse into a single model for many steps.
**Upsampling for balanced class ratios**
The oracle routing distribution was heavily skewed towards Nemotron 3 Ultra. A router that learned to always pick Nemotron 3 Ultra gets credit on three quarters of the dataset. We upsampled with replacement until the oracle routing distribution in the dataset was balanced. We observed that this allows the model to learn a decision boundary that actually distinguishes the Opus and GPT-leaning tail.
**Non-agentic vs. agentic router**
A router can either commit to a routing decision from the static task context (issue text + a one-shot codebase snapshot) or it can be given a bash tool with read-only access to the actual repository checkout, run a few targeted commands, then route. We trained both variants. The non-agentic router produces a reasoning trace and a single tool call with the routing decision; the agentic router can interleave bash calls with reasoning before routing.
Providing the model read-only tools and a 16K token budget allows the model to learn a routing policy that integrates more dynamic observation of the underlying codebase. In our experiments, we found the model learned routing rules that were bash-gated: the cross-cutting API rule fires only when the named symbol shows up in more than two source files, and the multi-stack rule fires only when the rule's symbol is consumed at two or more layers of the stack. Without bash, these rules collapse to surface heuristics. The non-agentic variant has to fall back to a precomputed snapshot of the codebase (truncated tree, file-extension counts, README excerpt, recent-commit log) and decide off the issue text alone. With similar seed policies, we observed the agentic router outperforms a non-agentic router.
**Binary reward vs. partial credit reward**
We experimented with a reward function that gave the router partial credit when the routed model tied the oracle on per-task pass rate: 1.0 for being the unique oracle pick, 0.5 for tying it on performance, 0.0 otherwise. In practice, partial credit collapsed the router onto Claude Opus 4.7. The reason is structural: Opus is the strongest constant policy in our panel, so on the bulk of tasks where the oracle's reward is achievable by more than one model, Opus is on the tied set. A router that always picks Opus collects 0.5 reward on a large share of the dataset and never has to learn the discriminative structure.
**Prompt optimization of the seed policy**
The router’s system prompt primes the model with a seed policy for RL training. We ran ablations with different seed policies based on the performance of an intermediate router checkpoint on the training set. Each variation adheres to the guidelines discussed in the capability analysis methodology. The qualitative routing criteria are very subtle, so it's a delicate balance of priming the router with a good seed prompt and not overfitting to the training data.
**Results**
The headline configuration for our best run is:
Component | Configuration  
---|---  
Algorithm| GRPO, ε=0.2, ε_high=0.28, no KL, no entropy bonus  
Optimizer| Adam (β=0.9 / 0.98), lr=5e-7 constant, weight-decay=0.1, clip-grad=0.5  
Rollout shape| 64 tasks per batch, 8 samples per task, GBS=512, response cap 16,384 tokens, T=1.0  
Reward| binary: 1.0 for the optimal model choice, 0.0 for any other valid model, −1.0 for no-route  
Over the course of this run, we see the agentic model router get closer to the oracle:
Cohen’s kappa measures the agreement of the two routers on specific tasks, and Total Variation Distance measures the closeness of the routing decision distributions.
Per-task agreement with the oracle is a strict yardstick. Many tasks are ties where several models would pass, so kappa gives the router no credit for picking a different-but-equally-valid model; the same reason we preferred binary over partial-credit reward. What matters for a routing policy is its position on the cost-quality frontier and how closely its decision distribution tracks the oracle's (the falling TVD), not whether it reproduces the oracle's pick task by task.
On held-out SWE-bench Verified tasks, routing is a real cost-quality tradeoff, not a single knob. Always using Nemotron 3 Ultra is cheapest (~$0.39/task) but leaves a meaningful pass rate on the table. Always using GPT-5.5 or Opus 4.7 buys more quality at roughly 3x the cost.
The trained router lands at ~76% pass — essentially GPT-5.5's quality for about 25% less cost. The oracle (label) point shows the ceiling if you could perfectly pick the best downstream model every time; the trained router closes much of the gap toward always-Opus quality without paying always-Opus price.
A natural comparison is to use a frontier model as the router itself: give GPT-5.5, Opus 4.7, or Nemotron 3 Ultra the same routing task and let it choose the downstream model. On our eval, none of them beat the trained specialist. A small 
model trained only to route outperforms every frontier model pressed into the same role.
*Qwen3.6-35B-A3B is the base model for the trained router
### **Example routing decisions**
1.
Example 1: Localized metaclass bug with single obvious fix site
**Task:** astropy__astropy-7166
**Issue summary:** InheritDocstringsInheritDocstringsInheritDocstrings fails for properties because inspect.isfunctioninspect.isfunctioninspect.isfunction returns false for property objects.
**Relevant repository signals:** router inspected /testbed/astropy/utils/misc.py,/testbed/astropy/utils/misc.py,/testbed/astropy/utils/misc.py, jumped to class InheritDocstringsInheritDocstringsInheritDocstrings (line 497), and reviewed only that local section.
**Model chosen by router:** nemotron−ultranemotron-ultranemotron−ultra
**Oracle label:** nemotron−ultranemotron-ultranemotron−ultra
**Routed rollout passed:** yes (chosenarmreward=1.0chosen_arm_reward = 1.0chosena​rmr​eward=1.0)
**Model router reward:** 1.0
**Explanation:** narrow patch surface and concrete failure mode imply that cheap/default arm should work; router and oracle aligned.
2.
Example 2: Django admin permissions regression across multiple internals
**Task:** django__django-11149
**Issue summary:** view-only users can still edit auto-created ManyToMany inlines in admin.
**Relevant repository signals:** router surfaced permission-related files/tests (`admin/helpers.py, options.py, templatetags/admin_modify.py, tests/admin_*`).
**Model chosen by router:** opus−4.7opus-4.7opus−4.7
**Oracle label:** opus−4.7opus-4.7opus−4.7
**Routed rollout passed:** yes (chosenarmreward=1.0chosen_arm_reward = 1.0chosena​rmr​eward=1.0)
**Model router reward:** 1.0
**Explanation:** cross-file permission semantics and protocol-level behavior favor the stronger model; router escalated correctly.
3.
Example 3: Complex ORM/GFK UUID bug
**Task:** django__django-11211
**Issue summary:** prefetch_related issue with GenericForeignKeyGenericForeignKeyGenericForeignKey when target model uses UUID primary key.
**Relevant repository signals:** router identified ORM internals complexity (generic relations + prefetch logic + PK-type handling).
**Model chosen by router:** opus−4.7opus-4.7opus−4.7
**Oracle label:** nemotron−ultranemotron-ultranemotron−ultra
**Routed rollout passed:** yes (chosenarmreward=1.0,bestarmreward=1.0chosen_arm_reward = 1.0, best_arm_reward = 1.0chosena​rmr​eward=1.0,besta​rmr​eward=1.0)
**Model router reward:** 0.0
**Explanation:** router decided that the task was sufficiently complex and cross-functional to escalate to Opus 4.7, but Nemotron 3 Ultra surprised to the upside.
### **Routing is only the first step**
The current router treats the three candidate models as fixed. But, in practice, they are not fixed.
The same data that trains the router can also identify where each model fails. If Nemotron 3 Ultra is already the oracle choice for a large fraction of tasks, it can be post-trained on the regions where it underperforms and move the entire frontier.
That is especially important for cost. As Nemotron 3 Ultra improves on SWE tasks while staying cheaper, the router should shift more traffic to it. The result is a compounding loop:
  1. Collect production rollouts
  2. Identify model-specific gaps
  3. Train a router over the current model set
  4. Post-train the most cost-effective model on its failure regions
  5. Update the router as the frontier changes

This is how multi-model systems should improve: not by treating model selection as a one-time benchmark comparison, but by continuously shaping both the router and the routed models.
### **Conclusion**
The next generation of agentic systems will not be built around a single model.
They will be built around portfolios of models, each with different strengths, weaknesses, latency profiles, and costs. The central infrastructure problem is deciding which model should act on which task.
For SWE-bench Verified, our early rollouts show that there is substantial headroom between the best constant model policy and an oracle routing policy. The oracle policy is more performant than every single-model policy, and it dominates the two closed-API options on both quality and cost. That means the routing problem is worth learning.
We are training a small router to recover that structure from task context. It sees the issue, repository signals, and a trainset-derived capability analysis, then chooses between Nemotron 3 Ultra, GPT-5.5, and Claude Opus 4.7. The reward is intentionally simple: choose the strongest model for the task, and if there is a tie, choose the cheapest.
This is the production shape we care about: better performance, lower cost, and a system that can adapt as the model frontier changes.
Nemotron 3 Ultra is particularly interesting in this setup. The oracle already routes a large share of tasks to it in our rollout set. And routing is not the end of the story. We can post-train Nemotron 3 Ultra on this task distribution to improve its SWE performance, then make the routed system cheaper and stronger by shifting more traffic toward it.
The future is multi-model, and the router is the control plane.