---
title: "Memory in the wild: how we use Context Engine on our own code"
date: MAY 8, 2026
authors: "SAM DENTON, DYLAN YU, RAYMOND FENG"
source: "https://appliedcompute.com/research/memory-in-the-wild"
---

[Last week⌝](/research/remember-refine-retrieve) we introduced Context Engine, Applied Compute’s system for remembering, refining, and retrieving enterprise context to build continual learning agents. This post is about what happened when we pointed it at ourselves.
Although the results are early, they show promising gains from using context derived from prior traces. Notably, using a Contextbase built over our own coding sessions, we were able to roughly **2x the rate of retrieving memories** critical to a coding agent’s task through continual learning in production. Additionally, on a small curated set of tasks where we found clear indication of memories being critical, agents were able to successfully use injected memories from the Contextbase to outperform the no-memory baseline.
### Introducing ACL-Wiki
For the past few months, we've logged every coding agent interaction at Applied Compute across Cursor, Claude Code, and Codex, and routed those traces into Applied Compute Logs (**`ACL`**)**,** a single log of how we actually build software. We then used our Context Engine to create an ACL Contextbase, and made the resulting Contextbase available to the coding agents through an MCP server. We call this loop **`ACL-Wiki`**.
The pipeline is the same [Remember, Refine, and Retrieve⌝](/research/remember-refine-retrieve) but specialized for code:
  1. **Remember** ingests every coding-agent trace.
  2. **Refine** extracts low-level memories from debugging sessions, builds higher-level procedural memories on top, deduplicates and prunes stale entries, organizes memories into a folder structure, and writes a top-level index.
  3. **Retrieve** exposes the Contextbase to the coding agent at runtime, supplementing whatever context it already has from the codebase.

On top of the base loop, we set up a _continual learning_ feedback tool where engineers can flag sessions where a memory should have been created, or where an existing memory was either useful or distracting. Those flags feed back into Refine, which updates the Contextbase daily.
### Benchmarking ACL-Wiki
To monitor improvements/degradations in ACL-Wiki, we tracked whether the retrieved memories were critical to the task via a metric we call the Critical Memory Rate. This shows the percentage of time that an LLM-as-a-Judge with full context of the trajectory believes that our Retrieve call returned information to the coding agent that was necessary for accomplishing the task effectively. For grading stability, we use majority vote@3 run on GPT-5.4-mini. We include an example of a graded trace with a positive critical score in the appendix. We filter by buckets with >15 ACL-Wiki retrieve calls.
At the start, the retrieved context from ACL-Wiki was relatively minimal lift over the coding agent's base performance. As we used it more (more traces, more engineer feedback), we saw the moving average of Critical Memory Rate climb from under 10% to around 20% over two weeks. Critical Memory Rate has a natural ceiling, as not every task needs institutional knowledge. But agents are judged on their weakest moments, not their average ones, and the long-tail tasks are exactly where institutional memory pays. Contextbase can help disproportionately to improve performance on those types of tasks. This is key to our thesis of integrating memory into enterprises: the more a system is used, the sharper its memory becomes on the decisions that matter most.
### Using Production to Build a Benchmark: ACLBench
Critical Memory Rate tells us direction, but it doesn't tell us when memory helps and when it hurts. So we built **`ACLBench`** : a hand-curated set of coding tasks drawn from the same production traces. This benchmark inverts the traditional model benchmark setup in that the entity being evaluated is the memory system, while the model is held fixed. With this framework, we can swap memory systems (or remove memory entirely) and compare directly.
We first split each production trace into **intent chunks** , i.e. segments of a conversation where the user introduces and resolves a single intent or goal. We filtered these chunks for intents that were self-contained within a repository (no external dependencies or API calls) to support replaying scenarios.
We then manually selected chunks with a clear need for memory so we could test if a memory system would be able to improve on an agent’s counterfactual trajectory.
For example, consider these two chunks:
  * A chunk where the user asks for a table, and then asks for the table to be rendered with purple text.
  * A chunk where the user asks for a table, and then asks for the table to be deleted.

We think a memory system _should_ form a preference memory from the first but not the second — tables in the future should default to purple text but should not default to being deleted.
We hand-picked roughly 25 chunks where the right behavior of a memory system was unambiguous. (Note: we found that larger scale datasets directly generated from LLM-as-a-judge filtration did not work well. Existing frontier models were not good judges for how valuable a task would be for distinguishing good and bad memory systems.)
For each selected chunk, we derive two pieces of data:
  1. The chunk’s raw trace which can be Remembered into a Contextbase.
  2. A task specification (user message, git hash, etc.) to seed a replayable scenario.

For the benchmark, we curate two types of tasks with different graders:
  1. **Memory tasks** where the task prompt tests the model’s ability to remember information learned from existing memories (most often from the actual trace for the associated chunk in production). We create an associated rubric that looks for the usage of certain memories in the solution path and rewards successful usage positively.
  2. **Distractor tasks** where either no useful memories are expected to be created but the model may be distracted by other existing memories, or where some useful memory could be created which may degrade the model’s performance on other tasks. We create an associated rubric that looks for usage of certain memories in the solution path and reward usage negatively.

Memory tasks measure the performance lift of a memory system, whereas distractor tasks measure regressions.
We re-ran each task with Claude Opus 4.6 in a minimal coding-agent harness, scoring 0.0 when the user’s task was not accomplished and otherwise scoring with the average of all criteria in the rubric. We then averaged results over SPI=3. The Contextbase was constructed by running a simple version of the Remember, Refine, Retrieve pipeline across all traces in the eval set.
We bucket the results by _why_ memory should help in the first place:
  1. **Reduce time-to-value through _documenting prior issues_.** Memories that capture how to do a recurring task — the same kind of memories that let teacher models distill best practices into student models with detailed SOPs and drive token-efficiency gains.
  2. **Expose steerability through _user preference_.** Memories that encode what a team or user wants — the editable surface where an enterprise can control the context their agent uses on every rollout, without retraining.
  3. **Solve incomplete or intractable environments through _external rules_.** Tasks that are _underspecified without memory_ , either because the relevant information lives in an SME's head or because the relevant data is too large to navigate from scratch. The representative example in our set: do not use LiteLLM, given the recent security breach.

The eval set we curate here is low in total samples (`n`) because code context is already extremely rich and frontier models’ coding capabilities are already strong enough to assume what the user wants. But as we see in the above results, where memories could plausibly be helpful, they are disproportionately so:
  1. **The Contextbase lifts every category.** Coding agents are willing to listen to external guidance when doing tasks.
     1. _User preference_ is particularly hard to satisfy by “chance” and easy to satisfy with proper context
  2. **Distractors don't cause regressions.** Coding Agents are able to ignore unhelpful context.
     1. _Note: the improvement over baseline on distractors was likely just due to noise in both Opus 4.6's ability to do the task and our LLM-as-a-judge._

### Why this matters
Across this two-post series, we've now used the same infrastructure (AC Context Engine) to apply custom Remember, Refine, and Retrieve pipelines against three different deployments:
  1. **Public enterprise benchmarks** ([APEX-Agents⌝](https://www.mercor.com/apex/apex-agents-leaderboard/), [GDPVal⌝](https://openai.com/index/gdpval/)) — up to 16.9% relative improvement and reasoning-effort amortized onto offline compute.
  2. **Live internal coding work at AC** (ACL-Wiki) — Critical % climbing steadily across the first week in production as the Contextbase learned from engineers’ feedback.
  3. **A targeted internal benchmark** (ACLBench) — memory's contribution decomposed by task type, with consistent gains on memory tasks and no significant regression on distractors.

The thesis is still the same: production traces are valuable, and most enterprises are throwing theirs away. We convert that golden resource into a Contextbase, plug it back into your agents, and watch as they get sharper every day.
If you are an enterprise looking to turn your production traces into your own specific advantage, reach out.
### Appendix: [ACL-Wiki] What this looks like in the wild
Here is a _prior-issue_ task from a positive critical judgement from a real rollout in production at AC (_Note: language is slightly edited to protect proprietary content_):
> Conversation: _Employee A,_ 2026-04-27 User query: "Can you add the argument to log rollouts to `run-model.py`? Save data to `PATH-{run-id}`"
ACL-Wiki Retrieve response (excerpt):
> Yes — but only add the new argument if it is not already the launcher default. For `train_*.py` launch scripts, the rule is: check the default in `main_config.py`, and if the desired value equals the default, omit the field entirely. If it differs, set it explicitly.  
>   
> So the change in `run-model.py` should be to add a debug-rollout-data argument pointing there, but only if that is not already the default value for the corresponding field…  
> [matched pages]  
>   
> [_Employee B_] In launch configs, omit fields whose value equals the default  
> [_Employee C_] Porting Logging Package runs page into console: cycles burned on inventing abstractions instead of mirroring the reference  
> [_Employee B_] Explanations: use concrete examples, lead with the high-level picture, stay concise but rigorous
Why the judge marked it critical (3/3, high confidence):
> "The retrieve supplied the load-bearing rule about omitting launcher fields that match defaults, and the user accepted the resulting edit without correction."
### Appendix: [ACL-Bench] What this looks like in our eval
Here is a _prior-issue_ task from ACLBench, drawn from a session at AC.
> **User:** Have it query for tasks before the cutoff
The relevant excerpt in the Contextbase shows not just the recommended pattern, but also an understanding of why:
> _Project convention — query patterns in server: services should use`Model.query(ctx)` for non-trivial queries rather than raw `ctx.db.query(Model)`. The query method is defined in `db/base.py` and preserves filtering based on `soft_delete` status, authorization checks against the authenticated context, and other mixin behaviors via the `_apply_filters` cooperative chain. Raw `ctx.db.query()` is generally discouraged._
**Without the Contextbase** , the agent reasons generically and gives generic advice:
> "For more complex queries, services should use the ORM query builder pattern (e.g. `ctx.db.query(Model).filter(...).options(...))` rather than raw SQL — it's composable, readable, and consistent across the codebase. I’m writing the query now."
Plausible, but wrong for _this_ codebase: it ignores the authorization and soft-delete chains and would silently introduce bugs. **With the Contextbase mounted** , the agent grounds itself in the project's actual convention, verifies it with grep, and produces:
> "Services should use `Model.query(ctx)` as their query base — this chains through `_apply_filters`, which preserves authorization checks, soft-delete filtering and other mixin behaviors. I’m writing the query now."
While the model itself didn’t get smarter, the agent was able to get the right context.