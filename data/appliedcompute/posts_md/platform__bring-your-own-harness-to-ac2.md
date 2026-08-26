---
title: "Bring Your Own Harness to AC2"
date: AUGUST 6, 2026
authors: "VINJAI VALE"
source: "https://appliedcompute.com/platform/bring-your-own-harness-to-ac2"
---

A production agent is a complex engineered system around LLMs. It includes deliberate management of context, tools, sandboxing, authentication, memory, and access to proprietary systems. Connecting that system to a post-training stack often requires porting the agent loop into a new runtime or building custom infrastructure to capture training trajectories. This work is expensive and can introduce **train-test mismatch** , where the policy is optimized in a lab that simulates the harness, and then struggles when faced with the nuances of production.
But what if instead of requiring users to adopt a new agent framework or re-instrument their harness with our tracing primitives, we could just replace the LLM response endpoint?
The harness can stay where it already runs, and the trainer has the same interface as inference. Behind the scenes, the trainer captures all the tokens and generation metadata needed for gradient steps, plus rich tracing and observability data inferred from the completions.
In this blog post, we’ll show how anyone can bring-your-own-harness to AC2 and train models inside it. AC2 attaches to the harness in two ways:
  1. A model endpoint for trainable policy generations;
  2. A lifecycle interface for starting rollouts, observing their status, and collecting gradable artifacts.

The agent remains as the complete production system, while training updates the underlying LLM policy that drives it.
### Two integrations: model API and rollout lifecycle
The primary integration seam is the **trainable model**. At the beginning of a rollout, AC2 supplies an OpenAI-compatible LLM endpoint and API credential, backed by the policy that’s actively being trained. The harness simply configures its existing LLM client to send the trainable policy’s requests to that endpoint; from the harness’ perspective, performing an RL rollout is no different from production inference.
The second integration is the **rollout lifecycle** wrapper. AC2 uses lifecycle entrypoints to initiate or continue a rollout, observe its execution until it reaches a terminal state, and collect the results required for grading. The harness retains full ownership over what context to send, when to call the model, which tools to invoke, how to manage state, and when the task is complete.
The entire Bring-Your-Own-Harness (BYOH) protocol is:
[code]
    submit(turn_input, llm_url, api_key, rollout_id=None) -> rollout_id
    get_status(rollout_id) -> status
    collect_output(rollout_id) -> artifacts
[/code]
This integration boundary is also the privacy boundary, as only the minimal data around LLM completions and grading needs to cross over into the training stack and all proprietary execution can remain in the customer’s stack.
### Turning model calls into training trajectories
First, AC2 supplies a specific OpenAI-compatible LLM API URL (and API key) for each individual rollout. This is how AC2 knows which model calls belong to which rollouts. The harness just needs to route its existing model requests to that endpoint; it does not need to emit any additional observability data.
The AC2 trace server maintains a data structure mapping the exact message trajectories, tokenization, log probabilities, and generation parameters across all currently ongoing rollouts. Treating each LLM request as an independent instance would risk inconsistent tokenization and lose the relationship between successive generations; instead, we reconstruct the rollout as a [sequence of append-only episodes⌝](https://www.appliedcompute.com/platform/scaling-rl-training-multi-agent-systems). We compare request prefixes to the history already recorded, and append only the newly sampled continuation, using structural prefix matching (conceptually similar to a KV-cache).
Through this mechanism, the captured completions become eligible training episodes. The training algorithm can mask, filter, or re-weight portions of the captured sequence as appropriate; the prefix matching ensures the underlying record is faithful.
Finally, we execute a grader, which is a function that acts over the full set of episodes plus any additional content retrieved from the environment via `collect_output`, and returns an overall scalar rollout score. The flexible nature of `collect_output` allows for arbitrary environment preparation before grading; for instance, we could run an entire sandboxed agent as the grader over files generated during the rollout, or we could export various deterministically-calculated metrics from the harness and compute a simple function over them.
In particular, the harness does not need to know how the result will be graded. The same rollout can be evaluated by different graders without changing the agent loop.
### Worked example with OpenCode on SWE-bench
Let’s dive into an example of the BYOH rollout lifecycle interface. Consider the OpenCode harness running on a SWE-bench style task. OpenCode itself already knows how to inspect a repository, call tools, edit files, and iterate toward a solution.
To be able to train a policy inside OpenCode, we build an AC2 adapter that launches OpenCode inside the task sandbox, configures its model client to use the rollout-specific AC2 endpoint, observes the process, and retrieves the resulting git patch for grading. Here is example pseudocode:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
[code]
    class OpenCodeHarness(BYOHProtocol):
        async def submit(
            self,
            llm_url: str,
            api_key: str,
            turn_input: SWEBenchTask,
            rollout_id: str | None = None,
        ) -> str:
            run = await sandboxes.start_or_continue(
                rollout_id=rollout_id,
                image=turn_input.image,
                repository=turn_input.repository,
            )
    
            await run.start(
                ["opencode", "run", turn_input.instruction],
                env={
                    "OPENAI_BASE_URL": llm_url,
                    "OPENAI_API_KEY": api_key,
                },
            )
    
            return run.id
    
        async def get_status(
            self,
            rollout_id: str,
        ) -> RolloutStatus:
    	    # returns "running" | "completed" | "errored"
            return await sandboxes.status(rollout_id)
    
        async def collect_output(
            self,
            rollout_id: str,
        ) -> object:
            patch = await sandboxes.download(
                rollout_id,
                "submission.patch",
            )
    
            return { "patch_to_grade": patch }
[/code]
Sandbox creation, image caching, and task-file transfer are omitted here as they are infrastructure details, not part of the harness contract.
These lifecycle operations fit around an arbitrary harness runtime. An adapter might call a customer-hosted API, invoke a Python SDK, or launch a CLI inside a sandbox. For example:
Harness surface| `submit`| `get status`| `collect output`  
---|---|---|---  
API client| `POST /rollouts`| `GET /rollouts/{id}`| Request signed artifact URLs  
CLI client in a sandbox| Start a process| Inspect process state| Download files from sandbox  
Python SDK client| Call `client.run(...)`| Call `client.status(...)`| Call `client.assets(...)`  
### Beyond a single chat conversation
Modern production agent rollouts are rarely as simple as a single append-only chat. Harnesses may compact context, delegate work to subagents, trigger retries, or implement orchestration across multiple models.
Because AC2 observes calls at the model boundary rather than owning the agent loop, these structures do not need to be flattened into a framework-specific conversation. Model calls remain grouped under the same rollout while preserving the distinct contexts in which they occurred.
With compaction, the harness can ask the same policy to summarize its current state under a different system prompt, then continue in a fresh context from that summary. Both the compaction and post-compaction generations pass through the training endpoint. This allows the model to learn not only how to solve the task, but what information it must preserve so that later generations can solve it, because the compaction episode itself participates in the training objective.
Delegation and multi-agent orchestration follow the same structure. A harness can create one or more subagents, give each a specialized prompt and context, and route their policy calls through AC2. Their executions become additional episodes in the rollout, and it’s up to the training algorithm how to implement credit assignment and loss masking.
### Bring Your Own Harness to AC2
AC2 (the Applied Compute Agent Cloud) ships with SDK primitives for our customers to build an adapter over their existing harness to train with it in just a few hundred lines of code. This is a critical step towards closing the loop between training and inference: now AC2 can orchestrate the full gambit of the model development lifecycle — from dataset development, to eval and model sweeps, to offline RL training, to inference and continual learning with self-distillation — staying true to your production harness.