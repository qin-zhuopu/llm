---
title: "Speeding up RL with high-leverage samples"
date: MARCH 24, 2026
authors: "AGASTYA GOEL, LINDEN LI"
source: "https://appliedcompute.com/research/speeding-up-rl-with-high-leverage-samples"
---

We learn the most from a problem when we struggle but eventually solve it. We learn what works and what doesn’t, preparing us for the next one. But not all parts of this process teach us the same amount: the rare flashes of insight teach the most.
Unlike humans, who attempt a problem once and then solve it or give up, language models generate many independent attempts, or rollouts. Naive reinforcement learning algorithms assume that all of these attempts contain the same amount of information, and thus use all of them to update the model. But just as humans learn the most from rare insight, models learn the most from rare rollouts. If we give a model one hundred attempts at a difficult math problem and it solves it only ten times, those ten attempts teach the model far more than the ninety others.
In this blog, we formalize this intuition and find that in a problem with a 10% success rate like the one above, each successful rollout is 81 times more valuable than a failed one! More generally, we introduce sample leverage, which quantifies how much training signal a rollout contains in the binary reward setting. Using it, we construct the leverage thresholding algorithm, which improves compute-efficiency by identifying and selectively training on high-leverage rollouts.
### Three sources of noise in the RL policy gradient
Researchers use large batches of rollouts to accurately estimate the policy gradient in each step of RL. Understanding the sources of noise in this gradient allows us to determine which rollouts give the cleanest gradient estimates.
For a given rollout, define its reward as R(τ)R(\tau)R(τ). Then, the [policy-gradient theorem⌝](https://papers.nips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html) gives us the gradient as:
∇⃗θ Eτ∼πθ[R(τ)]=Eτ∼πθ[R(τ)∇⃗θlog⁡πθ(τ)].\vec \nabla_{\theta}\ \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)] = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau) \vec\nabla_\theta \log \pi_\theta(\tau)].∇θ​ Eτ∼πθ​​[R(τ)]=Eτ∼πθ​​[R(τ)∇θ​logπθ​(τ)].
We can estimate the gradient via [REINFORCE⌝](https://link.springer.com/article/10.1007/BF00992696) as follows:
  1. Sample rollouts {τi}i=1n\\{\tau_i\\}_{i=1}^n{τi​}i=1n​ from our policy,
  2. Compute rewards R(τi)R(\tau_i)R(τi​) for each rollout,
  3. Estimate the gradient by averaging R(τ)∇⃗θlog⁡πθ(τ)R(\tau)\vec\nabla_{\theta}\log\pi_\theta(\tau)R(τ)∇θ​logπθ​(τ).

Let’s break down the error in this gradient estimate. Let the training distribution of input prompts be D′\mathfrak D'D′ and the real-world distribution be D\mathfrak DD. Say we sample nnn datapoints D1,D2,…,Dn∼D′D_1, D_2, \ldots, D_n \sim \mathfrak D'D1​,D2​,…,Dn​∼D′, and for each datapoint DiD_iDi​, we sample mmm rollouts τi1,τi2,…,τim.\tau_{i1},\tau_{i2}, \ldots, \tau_{im}.τi1​,τi2​,…,τim​. Our gradient estimate is then:
1nm∑i=1n∑j=1mR(τij)∇⃗θlog⁡πθ(τij)≈∇⃗θ(ED∼D;τ∼πθ,D[R(τ)]).\frac{1}{nm}\sum_{i=1}^n \sum_{j=1}^m R(\tau_{ij}) \vec \nabla_\theta \log \pi_\theta(\tau_{ij}) \approx \vec \nabla_\theta \left( \mathbb{E}_{D \sim \mathfrak D; \tau \sim \pi_\theta, D}[ R(\tau)]\right).nm1​i=1∑n​j=1∑m​R(τij​)∇θ​logπθ​(τij​)≈∇θ​(ED∼D;τ∼πθ​,D​[R(τ)]).
We’ll analyze this expression with the following three levels of gradient estimates:
  * Set v⃗τ\vec{v}_\tauvτ​ to be the gradient estimate of a _trajectory_ τ\tauτ, i.e. R(τ)∇⃗θlog⁡πθ(τ)\colorbox{e8f1ec}{$R(\tau)\vec{\nabla}_\theta \log \pi_\theta(\tau)$}R(τ)∇θ​logπθ​(τ)​.  

  * Set v⃗D\vec{v}_DvD​ to be the gradient estimate of a _datapoint_ DDD, i.e. Eτ∼πθ,D[v⃗τ]\colorbox{e4f2fc}{$\mathbb{E}_{\tau \sim \pi_\theta, D}[\vec{v}_\tau]$}Eτ∼πθ​,D​[vτ​]​.  

  * Set v⃗D\vec{v}_\mathfrak{D}vD​ to be the gradient estimate of a _distribution_ of datapoints D\mathfrak{D}D, i.e. ED∼D[v⃗D]\colorbox{f4ebf9}{$\mathbb{E}_{D \sim \mathfrak{D}}[\vec{v}_D]$}ED∼D​[vD​]​.

The error, or _noise_ , in our gradient estimate can be broken down into three components, corresponding to the three levels above:
MSE(θ,D′,D)=Eτ11,τ12,…,τnm∼πθ,D′[∣v⃗D−1nm∑i,jv⃗τij∣2]=1nmED∼D′[Varτ∼πθ,D[v⃗τ]]+1nVarD∼D′[v⃗D]+∣v⃗D−v⃗D′∣2.\begin{align*} \text{MSE}(\theta,\mathfrak D', \mathfrak D) &= \mathbb{E}_{\tau_{11}, \tau_{12},\ldots,\tau_{nm} \sim\pi_\theta, \mathfrak D'}\left[\left|\vec v_{\mathfrak D} - \frac{1}{nm}\sum_{i,j}\vec v_{\tau_{ij}} \right|^2\right] \\\ &= \colorbox{e8f1ec}{$\frac{1}{nm}\mathbb{E}_{D\sim \mathfrak D'} \left[\text{Var}_{\tau \sim \pi_\theta,D}[\vec v_\tau]\right]$} + \colorbox{e4f2fc}{$\frac{1}{n}\text{Var}_{D \sim \mathfrak D'}[\vec v_D]$} + \colorbox{f4ebf9}{$|\vec v_{\mathfrak D} - \vec{v}_{\mathfrak D'}|^2$} . \end{align*}MSE(θ,D′,D)​=Eτ11​,τ12​,…,τnm​∼πθ​,D′​​​vD​−nm1​i,j∑​vτij​​​2​=nm1​ED∼D′​[Varτ∼πθ​,D​[vτ​]]​+n1​VarD∼D′​[vD​]​+∣vD​−vD′​∣2​.​
These three terms correspond to _rollout_ noise, _datapoint_ noise, and _distribution_ noise, respectively. Many important RL optimizations reduce one or more of these noise sources:
  * Larger batch size: by sampling more rollouts per batch or more datapoints per batch, we can reduce our rollout or datapoint noise, respectively. In practice, we do not train on the entire dataset each step, so the noise does not precisely follow the above formula.
  * Higher data quality: with higher quality data, we align the train and real-world distributions more closely (reducing distribution noise) and can also reduce the datapoint noise if the values of v⃗D\vec v_DvD​**** are tightly clustered.
  * Accurate reward baselines: advantage estimators, such as [Group Relative Policy Optimization (⌝](https://arxiv.org/abs/2402.03300)[GRPO)⌝](https://arxiv.org/abs/2402.03300), reduce the rollout noise by modifying the quantity v⃗τ\vec v_\tauvτ​, typically by adjusting the reward of a trajectory based on the datapoint DDD.

Our work focuses on the first source of noise. We analyze the gradient variance of different trajectories and use them to define the _sample leverage_ ,__ which captures the _signal-to-noise_ ratio of an RL rollout. By only training on the highest-signal datapoints, we free up more resources for producing rollouts.
### Models learn more from rare outcomes
Depending on their reward, different trajectories provide gradient estimates of different magnitudes. Since higher gradient magnitudes correspond to higher signal-to-noise ratios, trajectories with different rewards have different noise levels.
Consider a single prompt with a binary reward (e.g., a math problem). RL traditionally optimizes the probability of success ppp: the probability that the model gets a reward of 1 on any given attempt. As a reminder, the policy gradient theorem gives:
∇⃗θp=Eτ∼πθ[R(τ)∇⃗θlog⁡πθ(τ)]\vec\nabla_\theta p = \mathbb{E}_{\tau \sim \pi_\theta} [R(\tau)\vec\nabla_{\theta}\log\pi_\theta(\tau)]∇θ​p=Eτ∼πθ​​[R(τ)∇θ​logπθ​(τ)]
Let’s analyze what happens if we condition on the value of R(τ)R(\tau)R(τ). We drop the subscripts for readability:
E[∇⃗log⁡π(τ)∣R(τ)=1]=∑τ∣R(τ)=1π(τ)∇⃗log⁡π(τ)P[R(τ)=1]=∑τ∣R(τ)=1∇⃗π(τ)P[R(τ)=1]=∇⃗pp.\begin{align*} \mathbb{E}[ \vec\nabla\log\pi(\tau) \mid R(\tau) = 1] &= \frac{\sum_{\tau \mid R(\tau) = 1} \pi(\tau)\vec\nabla \log \pi (\tau)}{\mathbb{P}[R(\tau) = 1]} \\\ &= \frac{\sum_{\tau \mid R(\tau) = 1} \vec\nabla \pi (\tau)}{\mathbb{P}[R(\tau) = 1]} \\\ &= \frac{\vec\nabla p}{p}. \end{align*}E[∇logπ(τ)∣R(τ)=1]​=P[R(τ)=1]∑τ∣R(τ)=1​π(τ)∇logπ(τ)​=P[R(τ)=1]∑τ∣R(τ)=1​∇π(τ)​=p∇p​.​
We can similarly condition on R(τ)=0R(\tau) = 0R(τ)=0 to get:
E[∇⃗log⁡π(τ)∣R(τ)=0]=−∇⃗p1−p.\mathbb{E}[ \vec\nabla\log\pi(\tau) \mid R(\tau) = 0] = -\frac{\vec\nabla p}{1-p}.E[∇logπ(τ)∣R(τ)=0]=−1−p∇p​.
Within a rollout, only some tokens meaningfully contribute to the reward and thus to the mean gradient. However, _all_ tokens contribute to the gradient noise. Thus, conditioning on the reward should not affect most tokens’ contribution to the gradient noise, so we posit that the noise is the same for all types of rollouts:
Var[∇⃗log⁡π(τ)∣R(τ)=1]=Var[∇⃗log⁡π(τ)∣R(τ)=0]=:V\text{Var}\left[\vec{\nabla}\log\pi(\tau) \mid R(\tau) = 1\right] = \text{Var}\left[\vec{\nabla}\log\pi(\tau) \mid R(\tau) = 0\right] =: VVar[∇logπ(τ)∣R(τ)=1]=Var[∇logπ(τ)∣R(τ)=0]=:V
where Var[x⃗]:=tr(Cov[x⃗,x⃗])\text{Var}[\vec{x}] := \text{tr}(\text{Cov}[\vec{x}, \vec{x}])Var[x]:=tr(Cov[x,x]) is the total variance. We will justify this assumption both theoretically and empirically. Specifically, it allows us to derive GRPO and provides the basis for an experimentally faster RL algorithm.
Before we get into that, let’s do some basic analysis of these formulas. Recall that the gradient estimate of a trajectory τ\tauτ is: 
v⃗τ=∇⃗log⁡π(τ)\vec v_\tau=\vec \nabla \log \pi(\tau)vτ​=∇logπ(τ)
Define the _noise_ of this gradient estimate as its deviation N⃗τ\vec N_\tauNτ​ from the mean, so that:
v⃗τ=∇⃗pp+N⃗τwhen R(τ)=1,v⃗τ=−∇⃗p1−p+N⃗τwhen R(τ)=0.\begin{align*} \vec v_\tau &= \frac{\vec \nabla p}{p} + \vec N_\tau \quad \text{when } R(\tau) = 1, \\\ \vec v_\tau &= -\frac{\vec \nabla p}{1-p} + \vec N_\tau \quad \text{when } R(\tau) = 0. \end{align*}vτ​vτ​​=p∇p​+Nτ​when R(τ)=1,=−1−p∇p​+Nτ​when R(τ)=0.​
For example, at p=0.1p=0.1p=0.1, the gradient signal-to-noise ratio is 9 times higher for a sample with reward 1 than for one with reward 0. This discrepancy allows us to selectively train on the samples with the highest signal while controlling the gradient noise.
### Deriving GRPO from relative gradient signals
In the previous section, we assumed that the gradient logprobs of rollouts with different rewards have the same noise. We’ll find that optimizing for the lowest gradient noise with this assumption leads us to GRPO.
Let τ0,τ1\tau_0, \tau_1τ0​,τ1​ be trajectories sampled from our model with rewards 0 and 1 respectively. Define the following estimators:
g^0=−(1−p)v⃗τ0g^1=pv⃗τ1.\begin{align*} \hat g_0 &= -(1-p)\vec v_{\tau_0} \\\ \hat g_1 &= p\vec v_{\tau_1}. \end{align*}g^​0​g^​1​​=−(1−p)vτ0​​=pvτ1​​.​
Both quantities are unbiased estimators of ∇⃗p\vec \nabla p∇p, with variances:
Var⁡[g^0]=(1−p)2VVar⁡[g^1]=p2V\begin{aligned} \operatorname{Var}[\hat{g}_0] &= (1-p)^2 V \\\ \operatorname{Var}[\hat{g}_1] &= p^2 V \end{aligned}Var[g^​0​]Var[g^​1​]​=(1−p)2V=p2V​
where V=Var⁡[N⃗τ]V = \operatorname{Var}[\vec{N}_\tau]V=Var[Nτ​].
Define the estimator g^=c0g^0+c1g^1\hat{g} = c_0\hat{g}_0 + c_1\hat{g}_1g^​=c0​g^​0​+c1​g^​1​ for weights c0,c1c_0, c_1c0​,c1​. We'll find the best way to choose these weights to get an unbiased, low-variance estimate of ∇⃗p\vec{\nabla}p∇p. 
  * Unbiased: E[g^]=(c0+c1)∇⃗p\mathbb{E}[\hat{g}] = (c_0 + c_1)\vec{\nabla}pE[g^​]=(c0​+c1​)∇p, so we must have c1=1−c0c_1 = 1 - c_0c1​=1−c0​ to get an unbiased estimate. 
  * Low-variance: We want to minimize the variance Var⁡[g^]=(c02(1−p)2+c12p2) V\operatorname{Var}[\hat{g}] = (c_0^2(1-p)^2 + c_1^2 p^2)\,VVar[g^​]=(c02​(1−p)2+c12​p2)V. Setting the derivative to 000:

ddc0[c02(1−p)2+(1−c0)2p2]=02c0(1−p)2−2(1−c0)p2=0c0c1=p2(1−p)2.\begin{aligned} \frac{\mathrm{d}}{\mathrm{d}c_0}\left[c_0^2(1-p)^2 + (1-c_0)^2 p^2\right] &= 0 \\\ 2c_0(1-p)^2 - 2(1-c_0)p^2 &= 0 \\\ \frac{c_0}{c_1} &= \frac{p^2}{(1-p)^2}. \end{aligned}dc0​d​[c02​(1−p)2+(1−c0​)2p2]2c0​(1−p)2−2(1−c0​)p2c1​c0​​​=0=0=(1−p)2p2​.​
Thus, for some normalization constant zzz,
c0=zp2c1=z(1−p)2g^=z(−p2(1−p)v⃗τ0+(1−p)2pv⃗τ1)=zp(1−p)[(1−p)v⃗τ1−pv⃗τ0].\begin{aligned} c_0 &= zp^2 \\\ c_1 &= z(1-p)^2 \\\ \hat{g} &= z\left(-p^2(1-p)\vec{v}_{\tau_0} + (1-p)^2 p\vec{v}_{\tau_1}\right) \\\ &= zp(1-p)\left[(1-p)\vec{v}_{\tau_1} - p\vec{v}_{\tau_0}\right]. \end{aligned}c0​c1​g^​​=zp2=z(1−p)2=z(−p2(1−p)vτ0​​+(1−p)2pvτ1​​)=zp(1−p)[(1−p)vτ1​​−pvτ0​​].​
In other words, the optimal estimate of the gradient given rollouts v⃗0,v⃗1\vec{v}_0, \vec{v}_1v0​,v1​ is proportional to (1−p)v⃗τ1−pv⃗τ0(1-p)\vec{v}_{\tau_1} - p\vec{v}_{\tau_0}(1−p)vτ1​​−pvτ0​​. These weights are **exactly** the ones GRPO assigns!
The math in this section scales to multiple rollouts. It can be shown that if we sample n0n_0n0​ and n1n_1n1​ rollouts with rewards 0 and 1, respectively, we should weight each rollout with reward 0 proportional to −p-p−p, and each rollout with reward 1 proportional to 1−p1-p1−p: the same weights as GRPO. Thus, assigning advantages to minimize gradient noise is equivalent to GRPO across a batch.
### Rollout value is captured by the sample leverage
As demonstrated above, the signal-to-noise ratio is:
E(b⃗)Var(b⃗)∝1p for samples with reward 1,E(a⃗)Var(a⃗)∝11−p for samples with reward 0.\begin{aligned} &\frac{\mathbb{E}(\vec b)}{\sqrt{\text{Var}(\vec b)}} \propto \frac{1}{p} &\text{ for samples with reward } 1, \\\\[8pt] &\frac{\mathbb{E}(\vec a)}{\sqrt{\text{Var}(\vec a)}} \propto \frac{1}{1-p} &\text{ for samples with reward } 0. \end{aligned}​Var(b)​E(b)​∝p1​Var(a)​E(a)​∝1−p1​​ for samples with reward 1, for samples with reward 0.​
Correspondingly, we can calculate how many samples with reward 1 yield the same ratio as a sample with reward 0. Since taking m samples increases the signal to noise ratio by m\sqrt mm​.
pm=1−pm=(p1−p)2\frac{p}{\sqrt{m}} = 1-p\\\ \boxed{m = \left(\frac{p}{1-p}\right)^2}m​p​=1−pm=(1−pp​)2​
For instance, if p=9/10p = 9/10p=9/10, each reward 0 sample is worth as much as 81 reward 1 samples. On the other hand, if p=1/10p = 1/10p=1/10, each reward 1 sample becomes 81 times as valuable as reward 0 samples. **This result is our key takeaway.**
Formally, we define the leverage of a sample as:
L(τ)={1−ppR(τ)=1,p1−pR(τ)=0.L(\tau) = \begin{cases} \frac{1-p}{p} & R(\tau) = 1, \\\ \frac{p}{1-p} & R(\tau) = 0.\end{cases}L(τ)={p1−p​1−pp​​R(τ)=1,R(τ)=0.​
The leverage has a few nice properties:
  1. The average leverage of samples from a given prompt is 111.
  2. The leverage of a sample is proportional to its GRPO advantage squared.
  3. The optimal gradient estimate from a set of samples I\mathfrak{I}I has variance proportional to (∑τ∈IL(τ))−1.\left(\sum_{\tau \in \mathfrak{I}} L(\tau)\right)^{-1}.(∑τ∈I​L(τ))−1.

Property 3 means that if we sample a group of 128 rollouts from the same datapoint and train on a subset __ of them with total leverage 64, we get the same train signal as having sampled and trained on 64 rollouts! Thus, the leverage is the effective number of samples we train on. **We can convert this property into an efficient RL algorithm by sampling many rollouts and selectively training on the ones with high leverage.**
### Discarding low leverage samples
Let’s analyze how the leverage scales as we train on an increasing number of datapoints. Suppose a problem has a probability of success p=0.2p = 0.2p=0.2. Then we can selectively train on rollouts with R(τ)=1R(\tau) = 1R(τ)=1, giving us more leverage per sample without introducing bias. For any datapoint, if we take the xxx rollouts with the highest leverage, their total leverage will be greater than xxx. Across different success rate distributions (simulated with beta distributions), we get the following plot:
Figure 1: The proportion of total leverage captured at each proportion of training data used for different success rate distributions.
Let’s examine some numbers for the uniform case. By using only 20% of the data, we already capture 60% of the leverage for a uniform success rate distribution. After we use more than 50% of the data, the graph is linear, and training on an extra datapoint only gains ≈0.4\approx 0.4≈0.4 leverage! We can exploit this tradeoff by allocating more compute resources towards generating rollouts and selecting the highest-leverage ones for training.
### How to use sample leverage to speed up RL
We introduce the _leverage thresholding_ algorithm:
  1. Set a _leverage proportion threshold_ ℓ\ellℓ _._
  2. When the inference engine returns a group of mmm rollouts from the same datapoint, reduce the list of rollouts to the smallest set which meets the leverage threshold ℓ\ellℓ __(i.e., has total leverage at least ℓm\ell mℓm where mmm is the group size). Note that we estimate the success rate and compute advantages before reducing our rollout list since the reward distributions of the original and reduced lists are different.
  3. Collect selected rollouts into a training batch and train on them.

By giving the training process less work to do, leverage thresholding allows us to shift compute from the training to the inference engines. The threshold ℓ\ellℓ __ controls the strength of this shift: lower values lead the training process to strongly prioritize high-leverage samples and discard the rest. Using a threshold ensures that every datapoint is represented in our training batch. If we just collected the highest leverage samples from across datapoints into a batch, some datapoints would have very few or no samples selected, reducing our effective dataset size.
We use the following train setup:
  * Advantage estimator: GRPO
  * Model: Qwen3-8B
  * Compute: One 8xB200 node
  * Algorithm: Fully asynchronous RL

The list of experiments is:
Run type| Training Process GPUs| Inference Engine GPUs| Leverage thresholds  
---|---|---|---  
Baseline| 3| 5| -  
Baseline| 2| 6| -  
Leverage thresholding| 2| 6| 0.88, 0.9  
Leverage thresholding| 1| 7| 0.5, 0.6  
In baseline runs, we find that with 3 GPUs, the training process outpaces the inference engine, and with 2 GPUs, it is slower. Thus, one of these options is the optimal baseline split for our workload. Leverage thresholds are set empirically to balance the training and inference speeds. (See the appendix for batch and dataset details.)
### Leverage thresholding leads to improved runs in practice
Training with the leverage thresholding algorithm results in each step containing less total leverage. However, leverage thresholding runs process more total leverage per unit time, leading to better eval performance.
All figures in this section use the following recipe for readability:
  1. We omit the baseline run with 2 train GPUs since it underperforms the baseline run with 3 train GPUs in all metrics.
  2. We believe that the differences between leverage thresholding runs with the same compute split are largely due to variance, so we plot the mean value and shade the range to represent runs with the same compute split.
  3. We use ‘base-x-y’ to denote a baseline run with xxx train GPUs and yyy rollout GPUs and ‘lev-x-y’ to denote the leverage thresholding runs with xxx train GPUs and yyy rollout GPUs.

Refer to the appendix to see each run’s performance individually.
The training process’ focus on high-leverage samples leads to faster steps, as shown in Figure 2. For runs with leverage thresholding, each train step has total leverage less than the batch size (768), so we also plot the cumulative leverage (Figure 3).
Figure 2Figure 3
Figure 2: The number of completed train steps vs time across compute allocations.
Both plots show that the thresholding leverage algorithm has better performance. Finally, every single leverage thresholding run had the same or better eval score as the baseline runs:
Figure 4: The mean eval reward of each group of runs vs time.
### Conclusion: additional ways to apply sample leverage
“Garbage in, garbage out” has always been true; that’s why researchers spend months painstakingly constructing quality datasets. But unlike identifying the best prompts—a largely qualitative task—identifying the best rollouts is easy. We have a formula for it! The leverage thresholding algorithm provides automatic trash disposal, exploiting the gap between batch leverage and batch size to get an efficiency win.
We hope that the formalism provided by sample leverage will lead to more exciting work. Here are some of the possible extensions:
  * Generalizing sample leverage past the binary reward setting is difficult since conditioning on a certain reward value leads to a biased estimate of the gradient. Thus, arbitrarily removing samples from a batch also biases the gradient. However, it may be possible to extend sample leverage to work with rubric-based rewards, where the reward is a sum of independent binary rewards.
  * Instead of using a fixed threshold ℓ\ellℓ __ as we did for our experiments, we could dynamically adjust ℓ\ellℓ __ at each step to keep both the training process and inference engines running continuously.
  * Deploying a model in production may produce more data than is feasible to train on. Prioritizing training on samples with the highest leverage allows for maximizing the signal extracted per datapoint used.

The leverage thresholding algorithm provides a knob you can turn to better utilize a finite pool of computing resources by increasing the speed of your training process, allowing you to allocate more compute towards sampling. More generally, sample leverage is a framework for the analysis and optimization of dataset construction. We hope it allows the community to post-train models effectively and efficiently.
### Appendix
****
##### **1\. Scaling leverage thresholding**
We also examined the performance of the leverage thresholding algorithm with five nodes. We were unable to optimize the compute or leverage threshold hyperparameters at this scale, but we observed clear improvements with the parameters used. We trained Qwen3-8B with both our baseline and leverage thresholding setups with one node for training and four nodes for sampling, with a leverage proportion threshold ℓ=0.9.\ell = 0.9.ℓ=0.9. Dataset details are further in the appendix. Our results suggest improved step time and effective sample processing speed:
Figure 5Figure 6
Figure 5: The number of completed train steps vs time for five-node runs.
The leverage thresholding run also exhibited better eval performance.
Figure 7: The mean eval reward of each five-node run vs time.
We found that the training process was much slower than the inference engine with this split, so there is room to improve the baseline by increasing the number of train GPUs. We also expect the leverage thresholding run to improve significantly with optimal hyperparameters. Despite the suboptimal hyperparameters, these results suggest that we can still selectively train on high-leverage samples for faster training at this scale.
##### **2\. Leverage thresholding shows gains across rollout lengths**
As the model learns math, it is able to reason more efficiently and uses fewer tokens per rollout. Shorter rollouts mean faster steps, so step times generally decrease throughout a run. However, we observed significant run-to-run variance in how much rollout lengths decreased, adding noise to our step time comparisons. To control for this variation, we compared the step time to the mean rollout length of that step. We also plotted the _effective step time_ by dividing the step time by the mean batch leverage proportion. Note that ‘lev-x-y-z’ refers to the leverage thresholding run with xxx train GPUs, yyy rollout GPUs, and a leverage threshold of zzz.
Figure 8Figure 9
Figure 8: The step time versus the mean length of rollouts in that step.
In both plots, we see an improvement from most leverage thresholding runs across most rollout lengths. Thus, the speedups are due to the algorithm itself and not rollout length variance.
##### **3\. Leverage thresholding balances the training and inference engines**
We use the _idle ratio_ of each run (that is, the proportion of the time the training process spends waiting for rollouts) to compare the relative speeds of the training and inference engines.
Figure 10: The idle ratio (proportion of time the training process spends waiting for rollouts) at each train step across runs.
In the ‘base-2-6’ run, the training process hardly ever waits, showing that it is slower than the inference engine. On the other hand, with 3 GPUs, the idle ratio is always positive, so the training process is faster than the inference engine. The runs with leverage thresholding have intermediate idle ratios, indicating that both engines progress at nearly the same speed. For any compute allocation where the training process is slower than the inference engine, we can tune the leverage threshold to balance their speeds.
##### **4\. Dataset and batch details**
We filtered out problems which were too hard or too easy from the DAPO math dataset by giving Qwen3-8B four attempts on each and removing any that it solved 000 or 444 times. We then used 204820482048 of the datapoints for training and 256256256 for evals. Each eval datapoint was run four times, and the reported eval score is the proportion of successes.
Our one-node runs used batches of 242424 datapoints with 323232 rollouts generated from each, while our five-node runs used batches of 323232 datapoints with 323232 rollouts generated from each.
##### **5\. Additional plots**
Earlier in the blog, we made plots more readable by compressing leverage thresholding runs with the same compute allocation into one curve. Here, we plot each run separately for the interested reader. Note that ‘lev-x-y-z’ refers to the leverage thresholding run with xxx train GPUs, yyy rollout GPUs, and a leverage threshold of zzz.
Figure 11Figure 12Figure 13Figure 14