---
title: "Unlocking Real-Time Bug Detection at Cognition"
date: MAY 11, 2026
source: "https://appliedcompute.com/case-studies/cognition"
---

> The training recipe was precisely tailored to our product and use case. Applied Compute's approach to dataset, environment, and harness construction gave us confidence that the model would perform well in the production setting with real users.
> Moritz Stephan
> Engineering Lead, Cognition
### Launching SWE-check
Cognition is the team behind Devin and Windsurf, the AI-native IDE. [One of their newest features is SWE-Check⌝](https://windsurf.com/blog/devin-review-windsurf), a real-time bug detection agent that reviews a developer's code upon invocation and produces structured bug descriptions that render natively in the IDE. Cognition’s vision is to give every developer an expert code reviewer operating in lock step, catching issues before they reach production.
Cognition tested every viable open-source and closed-source model in the SWE-Check harness. Opus 4.6 was the only model that met the quality bar to ship, but it was too slow and expensive for on-demand bug detection in the IDE.
The need for frontier performance served cheaply in real-time is what motivated the partnership with Applied Compute. The result is a model, SWE-check, that enables 10x faster bug detection than the frontier alternative. SWE-check is in production, powering [Quick Review⌝](https://windsurf.com/blog/devin-review-windsurf) in Windsurf.
Here is how the final trained model performed compared to frontier closed- and open-source models:
### **The SWE-check agent and its requirements**
Bug detection in a production IDE is not a standard code analysis task. The model fires whenever the user presses a CMD + U. Unlike normal coding agents that operate in a chat interface, the SWE-check agent reasons and calls tools en route to producing a structured output with bug descriptions and bug-fixes that render natively in Windsurf.
1.
Source
**Repository** : `block/goose`
**Commit** : `cd0b7d69`
**PR(s) fixing bugs that trace back to this commit:** [#5066⌝](https://github.com/block/goose/pull/5066)
2.
Bug 1: concurrency & threading - high severity
  * **Description:** The code iterated over the keys view returned by self.extensions.lock().await.keys() while holding the extensions mutex guard across the iteration. The loop body then awaited a call to read_resource_from_extension, which itself may attempt to lock the same self.extensions mutex. Holding a mutex guard across an await that leads to re-lock attempts causes a deadlock, since the original guard is not released before the re-lock is requested. This manifested as the extension manager hanging when trying to read resources from extensions.
  * **Fix:** Before iterating and awaiting into extension-specific logic, the code now collects the extension names into an owned Vec<String> by cloning the keys while holding the lock and then immediately releases the lock. The subsequent iteration runs over the collected names (no mutex held), and calls into read_resource_from_extension with a reference to each name. This prevents holding the extensions mutex across awaits and eliminates the reentrant lock attempt that caused the deadlock. A short explanatory comment was also added above the collection to document the reason.

3.
Ground truth bug-fix
During training, the model starts inside a sandbox with the repo checked out to the source commit, and then its job is to output bugs that it identifies with descriptions along with bug-fixes. These bugs are compared to the ground truth bugs for that source commit. 
The agent needs to be fast to keep developers in flow, precise to avoid false positives that erode trust, and intelligent to catch the kinds of subtle, context-dependent bugs that matter. The balance lies in avoiding what Cognition calls "The Semi-Async Valley of Death."
Off-the-shelf models sit at fixed points on the cost-latency-performance pareto frontier. Larger frontier models delivered high quality outputs but were too slow and expensive. Smaller open-source models were fast but missed too many bugs. No option satisfied both quality, cost, and latency constraints.
Reinforcement learning gives teams a mechanism to decide where they land on this pareto frontier. Cognition needed a model with frontier-level bug detection quality at a latency and cost compatible with real-time, high-frequency use in the IDE. Using Cerebras for inference enabled subtle thinking – thousands of tokens of deep – in a matter of seconds, before the model produces a final structured output.
### **Building a product-native training pipeline**
A central principle of this engagement was that the product harness and model training had to be deeply interlinked. Everything that went into the training run traced directly back to the production environment or feedback from users.
**Step 1: Dataset and task setup**
We first constructed a purpose-built dataset using open-source code data mapping source commits to the issues they introduced, curated to cover diverse bug types across languages and match the distribution Windsurf users would encounter in practice.
During training, the model starts inside a sandbox with the repo checked out to the source commit. It outputs the bugs it identifies with descriptions and fixes, which are compared against the ground truth bugs for that commit.
**Step 2: Training inside the production environment**
The model was trained inside a replica of the Windsurf environment with access to the same tools and execution context as the deployed product, ensuring that training gains translated directly to end-user experience. Windsurf customer code was not used for training; rather, the exact Windsurf harness was used along with code from public repositories.
This product-integrated approach shaped every training decision. For example, the reward function included latency penalties calibrated to user drop-off data from internal dogfooding. And as SWE-Check fires frequently, false positive sensitivity was treated as a first-order objective.
**Step 3: Iterative feedback from production**
Applied Compute and Cognition trained several models iteratively, building a tight feedback loop with dogfooding. Although significant effort went into optimizing the reward function, the product experience with the agent actually feels to use while working is what matters most.
This loop drove concrete changes. In one iteration, dogfooding revealed the model was flagging false bugs it could have resolved by simply looking up a variable's definition. The agent lacked tracing tools for finding definitions and references, so the team built and exposed these tools in both the Windsurf product and the training setup, then re-trained.
### **Designing the reward function**
The reward used in post-training determines the model's behaviors. Two key technical ideas underpin this system. The first is _reward linearization_ , which provides a sample-level reward that serves as a proxy for the population-level metric. The second is _two-phase post-training_ , which first maximizes capability and then aligns the model to product usage patterns.
##### **Reward Linearization**
We begin by formalizing the training setup. Each rollout τ\tauτ has its own set of ground truth bugs (possibly 0). We score a set of predicted bugs as follows:
  1. We first check if the bugs are scoped correctly with a simple LLM-judge pass. If any bug in the list is actually a conglomerate of two different issues, we set the score to 0.
  2. We then check if each of the predicted bugs in the list matches one of the ground truth bugs.
  3. The results of these checks allows us to compute a sample-level precision and recall, which we define as P(τ)P(\tau)P(τ) and R(τ)R(\tau)R(τ) These should always be numbers between 0 and 1. We handle edge cases as follows:
     * If there are no predicted bugs and no ground truth bugs, we set the precision and recall to 1.
     * Otherwise, if exactly one of the predicted bugs and ground truth bugs lists is empty, then we set the precision and recall to 0.

There are two reasonable ways to aggregate these scores over many samples: 
  * We could aggregate a global total count of true positives (TP), false positives (FP), and false negatives (FN) to compute a global precision and recall, then combine them into an fβf_{\beta}fβ​ [score.⌝](https://en.wikipedia.org/wiki/F-score)
  * We could average P(τ)P(\tau)P(τ) and R(τ)R(\tau)R(τ) over the samples to get an average precision and an average recall, then combine them into an fβf_{\beta}fβ​ score.

Since we would not want to bias the model to be disproportionately good at examples where there are a lot of ground truth bugs (at the expense of poor performance on examples where there are few / no ground truth bugs), we opt for the second choice.
Choice of β: Early iterations of the model used β=1 and produced many falsepositives, flagging many benign diffs as bugs during dogfooding. To mitigate this, wedecided to switch to β=0.5, emphasizing precision.\begin{array}{l} \text{\textbf{Choice of }} \boldsymbol{\beta}\text{\textbf{:} Early iterations of the model used } \beta = 1 \text{ and produced many false} \\\ \text{positives, flagging many benign diffs as bugs during dogfooding. To mitigate this, we} \\\ \text{decided to switch to } \beta = 0.5\text{, emphasizing precision.} \end{array}Choice of β: Early iterations of the model used β=1 and produced many falsepositives, flagging many benign diffs as bugs during dogfooding. To mitigate this, wedecided to switch to β=0.5, emphasizing precision.​
We define Rpop=Eτ[R(τ)]R_{\mathrm{pop}}=\mathbb E_{\tau}[R(\tau)]Rpop​=Eτ​[R(τ)] and Ppop=Eτ[P(τ)]P_{\mathrm{pop}}=\mathbb E_{\tau}[P(\tau)]Ppop​=Eτ​[P(τ)]. We ultimately want the model to increase the metric:
fβ=(1+β2)Ppop⋅Rpopβ2Ppop+Rpop.f_{\beta} = \frac{(1+\beta^2) P_{\mathrm{pop}}\cdot R_{\mathrm{pop}}}{\beta^2 P_{\mathrm{pop}} + R_{\mathrm{pop}}}.fβ​=β2Ppop​+Rpop​(1+β2)Ppop​⋅Rpop​​.
Given this global metric, what should our sample level reward then be? A key observation is that we cannot directly use
fβ(τ)=(1+β2)P(τ)R(τ)β2P(τ)+R(τ)f_\beta(\tau)=\frac{(1+\beta^2)P(\tau)R(\tau)}{\beta^2P(\tau)+R(\tau)}fβ​(τ)=β2P(τ)+R(τ)(1+β2)P(τ)R(τ)​
because averaging fβ(τ)f_{\beta}(\tau)fβ​(τ) does not yield fβf_{\beta}fβ​. This motivates our idea of reward linearization, where we compute a first order approximation of fβf_{\beta}fβ​ in terms of PpopP_{\mathrm{pop}}Ppop​ and RpopR_{\mathrm{pop}}Rpop​, so that the averaging does work out.
Since we have a good sense of the initial values of PpopP_{\mathrm{pop}}Ppop​, RpopR_{\mathrm{pop}}Rpop​ (call these initial values Ppop,initP_{\mathrm{pop,init}}Ppop,init​ and Rpop,initR_{\mathrm{pop,init}}Rpop,init​), and the initial distribution of TP/FP/FN rates, then we can approximate the fβf_{\beta}fβ​ value with a suitable first order linear approximation in PpopP_{\mathrm{pop}}Ppop​ and RpopR_{\mathrm{pop}}Rpop​:
fβ≈x(Ppop−Ppop,init)+y(Rpop−Rpop,init)+(1+β2)Ppop,init⋅Rpop,initβ2Ppop,init+Rpop,initf_{\beta}\approx x(P_{\mathrm{pop}}-P_{\mathrm{pop,init}})+y(R_{\mathrm{pop}}-R_{\mathrm{pop,init}})+\frac{(1+\beta^2) P_{\mathrm{pop,init}}\cdot R_{\mathrm{pop,init}}}{\beta^2 P_{\mathrm{pop,init}} + R_{\mathrm{pop,init}}}fβ​≈x(Ppop​−Ppop,init​)+y(Rpop​−Rpop,init​)+β2Ppop,init​+Rpop,init​(1+β2)Ppop,init​⋅Rpop,init​​
It is important that the first order approximation is done with awareness of the initial values of the TP/FP/FN rates. In our runs, the changes in TP/FP/FN rates did not change the resulting slopes drastically over the course of the run so we used a fixed linearization; our method could be generalized by recalibrating the first order approximation during training if some of the initial values deviate too much.
Then a valid sample-level reward function (since it averages to the desired fβf_{\beta}fβ​ approximation above) would be:
reward⁡(τ)=x(P(τ)−Ppop,init)+y(R(τ)−Rpop,init)+(1+β2)Ppop,init⋅Rpop,initβ2Ppop,init+Rpop,init\operatorname{reward}(\tau)=x(P(\tau)-P_{\mathrm{pop,init}})+y(R(\tau)-R_{\mathrm{pop,init}})+\frac{(1+\beta^2) P_{\mathrm{pop,init}}\cdot R_{\mathrm{pop,init}}}{\beta^2 P_{\mathrm{pop,init}} + R_{\mathrm{pop,init}}}reward(τ)=x(P(τ)−Ppop,init​)+y(R(τ)−Rpop,init​)+β2Ppop,init​+Rpop,init​(1+β2)Ppop,init​⋅Rpop,init​​
##### **Two Phased Post Training**
Our goal was to train a model with frontier performance that had a much better latency profile. We found that the most effective training approach split the process into two distinct phases. The two phases differ only in the reward function, with the rest of the training setup remaining exactly the same.
  1. **Capability maximization** : The reward function is the base reward function which we computed in the reward linearization section. By climbing this reward, the model focuses purely on maximizing bug detection skill and is not penalized for incremental latency. Capability maximization was the bulk of the overall training process.
  2. **Product alignment** : The reward function is the base reward function plus an additional “latency penalty”. To compute the latency penalty, we first estimated the latency of the rollout using the number of completion tokens and tool-calling turns. Then, we estimated the statistical distribution for how long it takes users to switch off of SWE-check after invoking it using dogfooding data from an early internal version of the SWE-check agent.

Time to next event after invoking SWE-check
Count
0s
137
1-5s
128
6-10s
56
11-20s
78
21-30s
39
31-60s
38
61-120s
35
>120s
27
140
120
100
80
60
40
20
0
Time bucket
This distribution was effectively a proxy for how much time we had to keep users in-flow. We then computed the CDF of this distribution and used it to define a penalty that scales with estimated latency. The CDF at a given time tells us what fraction of users would have already moved on by then.
We normalized the penalty so that it starts at 0 for instant responses and is 1 at the tail, then linearly interpolated between bucket midpoints.
Latency penalty
Estimated latency (s)
The product alignment reward pushed the model to shed redundant tokens and improve parallel tool-calling, while not sacrificing performance for latency beyond what was necessary for user experience. Product alignment was a much shorter phase than capability maximization in terms of training time.
This two-phase approach outperformed the alternative of training with a single combined reward function from the start. When capability and product constraints were optimized simultaneously, the model tended to converge on local optima: for instance, learning to be extremely fast but producing shallow analysis that satisfied the latency target but missed real bugs. Separating the phases allowed the model to first develop genuine understanding of the task, then learn to compress that understanding efficiently.
### **Why this matters beyond bug detection**
Many organizations have features or workflows where frontier model quality is required, but frontier model cost and latency make deployment impractical. The standard response is to wait for the next generation of models and hope the tradeoffs improve, or to ship a degraded version using a cheaper model. Neither option is satisfactory.
There is a third path. With the right training infrastructure, a dataset that faithfully represents the production task, and a reward function that encodes how the product actually needs to behave, enterprises can post-train a specialized model that occupies the exact point on the cost-latency-performance Parento frontier required.
The institutional knowledge required already exists inside a business: the product telemetry, user behavior data, domain-specific quality standards, etc. The work is in connecting that knowledge to a training process that can act on it. Model specialization through RL is a powerful tool to achieve frontier performance with a better latency, cost, and user experience profile that is deeply aligned with the product.
ABOUT THE COMPANY
Makers of Devin, the first AI software engineer. Cognition is building collaborative AI teammates that enable engineers to focus on more interesting problems and empower engineering teams to strive for more ambitious goals.
[Visit Site ⌝](https://cognition.ai/)
INDUSTRY
Engineering
CHAMPION
Moritz Stephan
SHARE