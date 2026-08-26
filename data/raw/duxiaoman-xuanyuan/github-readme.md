GitHub - Duxiaoman-DI/XuanYuan: 轩辕：度小满中文金融对话大模型

🤗 HuggingFace • 🤖 ModelScope • 🟣 wisemodel • 💬 WeChat

News
[12/27/2024]🔥开源XuanYuan-FinX1-Preview推理大模型
[9/6/2024]  🔥开源XuanYuan3-70B系列模型
[3/11/2024] 🔥开源XuanYuan-6B、XuanYuan-13B、XuanYuan2-70B系列模型
[1/19/2023] 🔥开源XuanYuan-13B-Chat模型
[11/1/2023] 🔥开源XuanYuan-70B-Chat模型及8-bit和4bit量化模型
[9/22/2023] 🔥开源XuanYuan-70B Base模型
[9/22/2023] 🔥开源60G高质量中文金融数据。Hugging Face
[9/22/2023] 🔥开源中文金融领域知识评估数据集 FinanceIQ。GitHub | HuggingFace
[5/21/2023] 开源度小满轩辕-176B大模型，在BLOOM-176B的基础上针对中文通用领域和金融领域进行了针对性的预训练与微调。是国内首个开源的千亿级中文对话大模型

目前发布的模型和下载链接如下：

基座模型 | Chat模型 | 8-bit量化Chat模型 | 4-bit量化Chat模型
XuanYuan-FinX1-Preivew | 🤗 🤖 🟣
XuanYuan3-70B | 🤗 🤖 🟣 | 🤗 🤖 🟣
XuanYuan-6B | 🤗 🤖 | 🤗 🤖 | 🤗 🤖 | 🤗 🤖
XuanYuan-13B | 🤗 🤖 | 🤗 🤖 | 🤗 🤖 | 🤗 🤖
XuanYuan2-70B | 🤗 🤖 | 🤗 🤖 | 🤗 🤖 | 🤗 🤖
XuanYuan-70B | 🤗 🤖 | 🤗 🤖 | 🤗 🤖 | 🤗 🤖
XuanYuan-176B | 🤗

技术文档：
XuanYuan3-70B
XuanYuan-6B
XuanYuan-13B
XuanYuan2-70B
XuanYuan-70B

## XuanYuan-FinX1-Preview

### 介绍
轩辕-FinX1是金融领域首个类GPT-O1推理大模型，采用创新的思维链+过程奖励+强化学习训练范式，显著提升逻辑推理能力，并可展示O1模型未公开的完整思考过程，为金融决策提供更深入的洞察。

### 技术路线
为了实现大模型具备类O1的推理能力，尤其是在金融领域复杂的决策分析场景中，我们提出包含三个关键步骤的技术方案：
1. 构建稳定的思维链生成模型（高质量COT/Answer数据合成）
2. 金融决策加强的双奖励模型（ORM采用对比学习和逆强化学习，PRM使用MCTS反向验证）
3. PRM和ORM双引导下的PPO强化学习微调

### 基准测试
在金融评测基准 FinanceIQ 上，轩辕-FinX1在CPA、银行从业资格、证券从业资格等10大类金融权威资格认证中，均超越了GPT-4o和开源模型Qwen2.5-72B。尤其是在精算师这一类别，将分数从37.5提升至65.7。

在通用评测中，轩辕-FinX1在GPQA(科学推理)、MATH-500(数学)和AIME2024(数学竞赛)等评测中超越了GPT-4o，与O1以及国内最新发布的推理版大模型共同位列顶尖梯队。

## XuanYuan3-70B

### 介绍
XuanYuan3-70B系列模型是度小满数据智能应用部团队推出的第三代大模型，以LLaMA3-70B模型为底座，采用大量中英文语料进行增量预训练，并利用高质量指令数据进行SFT和强化学习对齐训练。支持的上下文长度为16k。

### 技术创新
- 精细化数据组织：增量预训练和SFT阶段采用更精细的数据组织方式和动态调控策略
- 全能金融奖励模型（UFRM）：通用领域偏好对齐预训练 + 金融领域高质量专业数据微调，引入对比学习与逆强化学习
- 迭代式强化训练（PEI-RLHF）：预训练-评估-改进的迭代式方法

### 金融能力评测
XuanYuan3-70B-Chat模型整体表现媲美GPT4o，在金融事件解读、金融业务分析、投研应用能力等测量维度上超越GPT4o。

## XuanYuan-6B / XuanYuan-13B

从零开始预训练的大模型，采用类LLaMA架构。XuanYuan-6B在FinanceIQ金融评估数据集上的性能超越GPT4。

## XuanYuan2-70B

基于XuanYuan-70B基座模型，使用更多高质量语料继续预训练和指令微调，并进行RLHF训练。支持上下文长度达到16k。

## XuanYuan-70B

基于Llama2-70B进行中文增强，扩充词表，经过大量通用+金融领域中文数据增量预训练。预训练上下文长度扩充到8k和16k，是首个在70B参数量级上达到8k及以上上下文长度的开源大模型。

## 开源金融数据集 FinCorpus
语料大小约60G：
- announcement_data.jsonl: 上市公司公告 (20G)
- fin_news_data.jsonl: 金融资讯/新闻 (30G)
- fin_articles_data.jsonl: 金融资讯/新闻 (10G)
- fin_exam.jsonl: 金融试题 (370M)

## 轩辕-176B：首个千亿级中文金融对话模型
基于BLOOM-176B针对中文通用领域和金融领域进行预训练与微调。国内首个开源千亿级中文对话大模型。

### 金融领域效果评测
轩辕在主流四种开源大模型比较中，赢得150次回答中63.33%的胜率。

### 通用领域效果评测
利用200道多元化问题评测，轩辕有71%的问题表现不亚于ChatGPT。

## 相关论文
- XuanYuan 2.0: A Large Chinese Financial Chat Model with Hundreds of Billions Parameters
- Self-QA: Unsupervised Knowledge Guided Language Model Alignment
- CGCE: A Chinese Generative Chat Evaluation Benchmark for General and Financial Domains

## 免责声明
对于轩辕模型生成的言论，不承担任何责任。使用者需自行承担潜在风险。
