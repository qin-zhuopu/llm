---
title: "Scaling RL training in the age of multi-agent systems"
date: JULY 28, 2026
authors: "RAYMOND FENG"
source: "https://appliedcompute.com/platform/scaling-rl-training-multi-agent-systems"
---

At Applied Compute, we think about three levers to pull to build the best agents: the model, the context, and the harness. Independently optimizing each of these components can yield significant performance improvements; jointly optimizing model, context, and harness is how we achieve state of the art results.
Traditional model optimization stacks focus on single sequences of tokens that do not capture the full task-level unit of work that models are now evaluated on. This limitation means that training on tasks that involve subagents or compaction are either avoided or extremely awkward. We have built our platform, the [Applied Compute Agent Cloud (AC2)⌝](https://www.appliedcompute.com/#platform), around the premise of evaluating and optimizing agents for full, end to end task performance. We support arbitrarily complex orchestration logic for task attempts that involve the ability to spawn subagents backed by the same model, multi-response collection, transient messages, and compaction. Using AC2, enterprises can train specific models in custom harnesses tuned for their specific use-cases.
Subagent ToolsMulti-Response CollectionTransient MessagesCompaction
### Native AC2 support for task level traces
The AC2 platform natively accommodates all different shapes of harnesses. We introduce a new framework that keeps track of agent state across all interactions for a single task (even across multiple conversations), which we call a trace. Each attempt at a task produces one trace. Task level outcomes are the level at which agents are evaluated, so they must also be the level at which agents are monitored and trained.
For each task, we keep track of a list of episodes which are append-only sequences of messages; these episodes are first class platform primitives that together can be thought of as a single trace. These episodes preserve the full expressibility of all possible harnesses — harnesses which require forking or modifications of previous messages simply need to start new episodes for each instance of forking or message mutation.
Below we show an example from our training for Harvey's LAB benchmark: [training a legal agent with Applied Compute⌝](https://www.harvey.ai/blog/training-a-legal-agent-with-applied-compute).
Above, we can see the AC2 platform keep track of the different episodes that result from running the agent in a compaction harness. Although there are multiple different conversations (a combination of agent conversations where work is being done and compactor agent conversations where the previous agent progress is summarized), they are all treated as a unit under the same task attempt by AC2.
#### One loop, all possible orchestration methods
The logic for managing episodes and driving agent progress end to end on a task lives in an AC2 `Orchestrator`. It implements one core function, `orchestrator.run`, which specifies the logic for sending completion requests to the agent between different user messages. AC2 comes with example implementations of the various aforementioned flavors of orchestration, which can all be used within the same, fully general loop:
1
2
3
4
[code]
    turn_input = await user.respond(orchestrator.env, orchestrator.trace)
    while turn_input is not None:
        await orchestrator.run(turn_input)
        turn_input = await user.respond(orchestrator.env, orchestrator.trace)
[/code]
The default behavior of `orchestrator.run` is to generate agent completions and respond with the appropriate tool call responses from the environment until an answer message is outputted and the orchestrator is ready for a new user message, all within a single episode.
However, the orchestration behavior can be customized with more complex methods such as compaction. The `orchestration.run` logic can involve setting up multiple episodes and combining them arbitrarily. For example, a simple implementation of compaction might look like:
1
2
3
4
5
6
7
8
[code]
    async def run(self, turn_input):
        """Simple compaction `orchestrator.run` implementation."""
        await self.session.run_turn(self.current_episode, turn_input)
        if context_tokens(self.current_episode.get_items()) > BUDGET:
            memo = await summarize(self.session, self.compactor, self.current_episode)
            self.current_episode = self.session.start_episode(
                self.agent, episode_start=[Message(role="user", content=f"{self.task}\n{memo}")]
            )
[/code]
Regardless of the orchestrator behavior, the above fully general loop allows us to reuse the production agent loop efficiently in training.
### How training works under the hood
The task-level features of AC2 shown so far give insight on task-level monitoring and evaluation for agents. Here, we demonstrate how the append-only episodes generated from the single general loop above translate cleanly to an efficient training backend.
#### Background on traditional RLVR
Traditionally, RLVR training involves assigning a scalar reward to a conversation. The conversation may involve many messages, some of which are generated by the agent, while the rest are generated by the user or by the environment.
A loss mask is applied to the conversation so that during training, the gradient signal only flows through the tokens that were generated by the agent itself. Mechanically, we do a forward pass in the training engine over the whole sequence of tokens in the conversation to compute the logprobs of _all_ the tokens in the sequence, then do a backward pass on a loss that is computed only from the logprobs of the agent-generated tokens.
#### Generalizing to multiple segments
The information that ultimately matters for doing backpropagation is the logprobs computed by the training engine forward pass(es) on the agent-generated tokens. What if we wanted to do training where we have one scalar reward for an entire task's trace, but that task's trace consists of multiple conversations?
This requires us to change our frame of reference from traditional RLVR. We can view the conversation and loss mask approach from the previous section as simply an optimization that reduces the total number of training forward passes on the following less-sophisticated but equivalent approach: for every _request_ sent to the agent, we record a new segment that has a loss mask which is 0 for all tokens in the input and 1 for all tokens in the agent's output.
For a single task, we assign the single scalar reward to all the segments in that tasks' trace. We then say that the loss contributed by that task is a weighted average of the losses that we get from each of these individual segments. We take the weights to be proportional to the number of agent generated tokens in each segment.
**Note:** the logprobs computed for each of the agent output tokens from this approach and the traditional approach are the exact same! It's just that this approach requires two separate forward passes in the training engine to compute the same logprobs as before, which is why we say that the traditional RLVR approach can simply be thought of as an optimization on top of this more basic approach. This optimization view of combining segments corresponds exactly to our definition of episodes in AC2: we only support append-only episodes because they correspond exactly to a set of requests that can be combined into a single forward pass.
#### Example: putting it together for training with compaction
We can take the idea from the previous section and apply it to training with a compaction orchestrator. Naively, we get something like this with one segment per request to the agent completion endpoint:
The final form of training with compaction involves bringing back the optimization from earlier. Clearly, there are segments here which are parts of the same conversation, and we would want to collate them together to avoid doing redundant forward passes in the training engine. These correspond one-to-one to the concept of episodes that AC2 natively tracks. So we ultimately end up with something like the following, where there is one segment per episode:
We assign the same task level scalar reward to all segments and then weight each segment by the total number of agent output tokens in that segment.
### An age of agents
We are entering an age of agents that autonomously drive tasks end to end. As such, agents must be evaluated, monitored, and optimized for results at the task-level. However, enterprises require custom orchestration logic for many of their specific tasks, whereas existing traditional model optimization stacks are built for updating the model based on rewards at the level of a single sequence of tokens.
We built AC2 to bridge this gap between task-level outcomes and single-conversation model optimization. AC2 bakes in these production metrics as first-class citizens: evaluate, inference and train your model on a consistent, task-level signal that aligns with outcomes your users care about.