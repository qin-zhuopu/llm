---
title: "Automating Merchant Onboarding at DoorDash"
date: FEBRUARY 17, 2026
source: "https://appliedcompute.com/case-studies/doordash"
---

> "AI has long been core to how DoorDash helps merchants succeed. By encoding our quality standards directly into model training, we scaled our internal expertise and raised the bar on menu accuracy on the platform."
> Andy Fang
> Co-Founder of DoorDash
DoorDash is a global leader in food delivery, with a core focus on helping merchants run their businesses seamlessly. During onboarding, DoorDash enables merchants to go live in as little as one day by using AI to generate highly accurate menus. Menu accuracy is critical because it impacts whether orders run smoothly, restaurants prepare the right items, and customers get what they ordered.
A joint effort between George Ignatius (DoorDash ML Engineer), Ying Yang (DoorDash Head of Merchant ML), and the Applied Compute team
### Understanding the Problem
DoorDash had already built a sophisticated AI system that automatically converts photos, PDFs, and text menus into structured listings during merchant onboarding, enabling restaurants to get on the platform and start receiving orders immediately.
The team holds an extremely high accuracy bar for any menu created through their AI system, but the sheer diversity of real-world menus pushed the technology to its limit.
> "The existing AI automation system handled most of the menus well, but there was always a long tail of messy menus with hard-to-summarize styles. We relied on internal human experts, and recognized the impact of improvement efforts started to become marginal.” 
> Ying Yang
> DoorDash Head of Merchant ML
DoorDash and Applied Compute realized that structured menu generation is hard to build a unified standard operating procedure for – even human experts had conflicting views on it. However, verification given a structured menu output and ground truth was much easier for human experts to agree upon. So the challenge then became building an automated grader that matches the way human experts do verification, which then could be trained against using reinforcement learning.
### Calibrating an Automated Grader
Building an extremely calibrated grader is critical in reinforcement learning, since the grader is what determines the rollouts that are positively or negatively reinforced. In particular, it is important for the grader to be (a) aligned with ground truth grading from human experts so that training against it gets closer to the desired state and (b) self-consistent so that the training process isn’t noisy and inefficient.
Working onsite at DoorDash’s Sunnyvale office to translate production QA labels into an automated grader
DoorDash’s high-quality quality assurance (QA) requirements, process, and human experts were instrumental in jumpstarting and then building the automated grader. Applied Compute’s tools helped quickly ladder-climb an effective grader setup that progressively became more aligned and self-consistent with the way human experts did verification.
> “The grader encoded the same rules our reviewers use, including the judgment-heavy edge cases. That gave us a reliable yardstick for reward function quality during model training.”
> George Ignatius
> DoorDash ML Engineer
Applied Compute’s product stack, including experiment tracking, automated failure detection, and grader calibration, enabled rapid iteration and surfaced deep domain knowledge previously embedded only in the DoorDash team’s experience. The result was an automated grader that reliably captured DoorDash's quality standards and could score model outputs automatically during training.
### Training a Model Against DoorDash’s Definition of Quality
Once the automated grader was reliable, it became the reward function for training a new menu error correction model to reduce menu error rate. Applied Compute's system took DoorDash's existing structured output and improved upon it, using reinforcement learning to maximize accuracy while meeting DoorDash's latency, cost, and reliability constraints. Together, the companies instrumented the system to monitor model performance across different menu error types, and tested multiple base models and training recipes to meet production requirements.
During training, the automated grading system scored the model’s structured output and determined the different types of errors based on DoorDash’s menu style guidelines, ultimately converting the errors into a single reward signal and creating a feedback loop that drove reliable improvements.
Below is a very simple example from the model’s chain-of-thought as it learned more subtle, relevant thinking over the course of training about how to correctly structure menu hierarchies:
[code]
    So they are different: one is dinner (with rice, beans, salad) and the other is just tacos (no side).
    
    We have two categories: one for "Taco Dinner" (with side) and one for "Tacos" (without side).
[/code]
### To Production and Beyond
DoorDash had confidence in moving forward with production testing due to the strong RL training performance, consistent offline results, and tracked online metrics.
Once the model showed strong and stable automated results, the team moved to stricter offline validation with human graders reflecting production conditions. DoorDash then ran an A/B test against their baseline system on a large sample of production menus. Human reviewers graded both versions and confirmed the gains were real.
In the test, the share of low-quality menus fell by roughly 30% relative to the baseline.
With automated and human validation aligned, the work moved to production. Applied Compute delivered a production-ready library that integrated directly into DoorDash’s codebase while meeting latency, robustness, and security constraints.
DoorDash has rolled out the error correction model to all menu traffic in the USA. As a next step, continuous performance monitoring can be used to feed production corrections back into training, establishing a repeatable flywheel for DoorDash to improve systems by turning judgement into an automated training signal.
ABOUT THE COMPANY
DoorDash is a technology and logistics company that started with on-demand door-to-door delivery. It empowers local businesses to connect with people through their platform of diners and dashers.
[Visit Site ⌝](https://about.doordash.com/)
CHAMPIONS
Ying Yang
George Ignatius
SHARE