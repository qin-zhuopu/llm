---
title: "Ari, Applied Compute's in-house AI research agent"
date: AUGUST 12, 2026
authors: "ANIRUDDH SRIRAM"
source: "https://appliedcompute.com/platform/ari"
---

At Applied Compute, our frontier post-training stack lets us train models for customers quickly and efficiently. But across our engagements, we noticed that researchers were spending a lot of their time operating the research loop rather than advancing it.
For a post-training researcher, much of the day goes to qualitative work just to confirm a run is on track. That might mean combing through thousands of agent traces to understand why a model learned a particular tool calling behavior, investigating a grader that's being hacked, or comparing eval data points across steps to see how behavior changed over the course of a run. The work is necessary, but much of it is repetitive and well suited for automation. What started as a shared set of Claude and Codex skills became far more powerful once we made it native to our platform, AC2.
### Introducing Ari
Applied Research Intelligence (Ari) is our in-house AI researcher. It integrates deeply with the AC2 Platform and SDK, serving as the intelligence layer that turns this stack into an increasingly autonomous research system.
Today, our researchers use Ari to sift through gigabytes of logs to find evidence of unhealthy behavior, remember what the team has learned from past experiments, and produce styled plots and reports as customer deliverables. Tomorrow, Ari will own more of the research loop by designing experiments, launching and monitoring runs, analyzing results, and recommending what to try next.
Ari gives every researcher leverage to spend less time monitoring runs and more time asking insightful questions to design better experiments. Our customers can use Ari as well, giving them more visibility into the models we build together.
### The shape of Ari
Ari uses the same tools as our researchers. Today, this includes curated skills, subagents, a dedicated sandbox, wandb access and memory across runs.
**Session workspace.** Each Ari session spawns an AC2 sandbox initialized with code from the run, including the environment and orchestration code specific to the run. The runtime image contains the AC2 SDK and CLI installed, so Ari can download traces, view datasets, or kick off evals.
**Compounding memory.** In each project, Ari connects to a shared AC2 Contextbase where it can read and write wiki pages. This wiki is used to remember project-specific quirks like “The PythonGrader is unreliable and its scores should be ignored when you analyze runs”. As Ari continues to write to this wiki, it becomes a lot more intelligent and delivers better responses to researchers.
**Dynamic analysis workflows.** Ari writes custom workflow scripts on demand to spawn dozens of specialized subagents that investigate traces in parallel, test hypotheses, and synthesize findings into actionable research direction. Fanning out subagents over traces is great for performing tool call analysis, identifying reward hacking, or comparing behavior across train steps.
**Artifact generation.** Every researcher produces a report summarizing key findings from their hero runs. Ari uses curated `/plot` and `/generate-report` skills to produce graphs, diagrams, presentations, and reports that you can directly publish to the train run. Ari also proactively generates a summary report for each train run on our platform.
**Slack integration.** We use this to alert researchers as well as start Ari sessions with Slack thread context.
### Grounded in real work
We built Ari around how real enterprise post-training work happens. Every engagement starts with writing code (agent harness, environment, graders), monitoring runs, looking at traces, and producing artifacts. Ari’s sandbox gives it a workspace to iterate on code and write reports.  
Once it kicks off a run, Ari monitors it by watching the same wandb and system metrics our researchers use. When the run is finished, dynamic workflows let Ari subagents look at traces and derive insights to inform the next experiment. For every run, it can produce a report or charts using a set of curated skills researchers already use to make artifacts.
To illustrate this, let’s look at an example of how Ari worked alongside a researcher for a real run. A researcher launched a run which Ari started monitoring, and then pinged them with this error:
Due to the alert, the researcher was able to terminate their run and ask Ari what the core issue was.
Ari correctly identified that their rollout concurrency was too high, causing an inference engine’s request queue to become overloaded with requests. We can also see that Ari recorded this as a project memory for future runs it may babysit or kick off.
Ari then kicked off a new run by fixing the training config to lower concurrency, and monitored the new run until it went to completion!
On the successful run, Ari was able kick off a subagent workflow to analyze traces and model behavior. We can see it references specific traces we should look at, which we can pull up right beside the chat in our platform.
Here, Ari found and referenced a passing and failing trace where the model learned to correctly enforce uniqueness constraints for `in_bulk()` as enforced by Django and also run tests.
To make it easy for the researcher, Ari produced a neat run report that summarized key findings and recommendations for what to try next.
Ari proactively generates a structured report when the run completes. The report serves as a neat final deliverable for the researcher to understand their run at a glance with key metrics highlighted.
### Applied research at scale
Ari leverages our proprietary research expertise via detailed skills it can apply across experiments. As Ari becomes more capable for our internal researchers, it also becomes a powerful platform offering that gives every AC2 user access to the same workflows, tools, and accumulated judgment.
The future of specialized models will be shaped by who can learn fastest from every experiment. Ari turns that learning into a system that compounds. Every run makes the researcher faster, and every researcher makes Ari better.