# 风乌

> 来源: [https://www.shlab.org.cn](https://www.shlab.org.cn)
> 抓取时间: 2026-08-25
> 公司: 上海人工智能实验室

---

* [首页](/)
* [科学研究](/research)

  [了解更多科学研究成果](/research)

  [Intern-S1](/intern-ai)

  『书生』科学多模态大模型

  [Intern-Discovery](https://discovery-home.intern-ai.org.cn/home)

  『书生』科学发现平台

  [Intern-Robotics](https://internrobotics.shlab.org.cn/)

  『书生』具身全栈引擎

  [Intern-SafeWork](https://ai45.shlab.org.cn/)

  『书生』SafeWork 安全技术栈

  [司南](https://opencompass.org.cn/)

  大模型开源开放评测体系

  [OpenDataLab](https://opendatalab.org.cn/)

  人工智能开放数据平台

  ${ v.tags || '最新动态' }

  ## ${ v.newstitle }${ v.tags || '推荐新闻' }

  ## ${ v.newstitle }
* [科研动态](javascript:void(0))

  [### 新闻动态](/info)

  感知行业动向，同创生态繁荣

  [了解更多](/info)

  [### 科研活动](/event)

  紧跟前沿趋势，共推技术变革

  [了解更多](/event)

  ${ v.tags || '新闻动态' }

  ## ${ v.newstitle }${ v.tags || '科研活动' }

  ## ${ v.newstitle }
* [开源开放](/open)

  [了解更多开源项目](/open?tab=model)

  [模型](/open?tab=model)[工具](/open?tab=tool)[算法](/open?tab=algorithm)[数据集](/open?tab=dataset)[评测集](/open?tab=evaluation)

  [## InternVL

  2024.05.09

  9.4k](https://github.com/OpenGVLab/InternVL)[## MinerU

  2025.11.06

  48.7k](https://github.com/opendatalab/MinerU)[## LMDeploy

  2025.10.30

  7.2k](https://github.com/InternLM/lmdeploy)[## InternLM

  2024.01.02

  7.1k](https://github.com/InternLM/InternLM)[## OpenCompass

  2025.10.20

  13k](https://github.com/open-compass/)[## XTuner

  2025.07.11

  5k](https://github.com/InternLM/xtuner)

  ${ v.tags || '新闻动态' }

  ## ${ v.newstitle }${ v.tags || '科研活动' }

  ## ${ v.newstitle }
* [关于我们](/aboutus)
* [加入我们](/joinus)

  [查看更多职位列表](/joinus/social)

  [### 社会招聘和校园招聘](/joinus/social)

  诚邀全球有志于从事人工智能、大模型、具身智能、安全可信AI、Al for Science、基础平台、创新链、管理支撑等领域的青年人才加入，共创AGI美好未来。

  [了解更多](/joinus/social)

  [### 招生信息](/enrollment)

  自2022年起，上海AI实验室与北京大学、清华大学、复旦大学、上海交通大学、同济大学、中国科学技术大学、浙江大学等十余所顶尖高校共同开展联合培养博士生专项工作。

  [了解更多](/enrollment)

  ${ v.tags || '招聘动态' }

  ## ${ v.newstitle }

---

> 补充来源: [https://arxiv.org/abs/2304.02948](https://arxiv.org/abs/2304.02948)
> 日期: 2025-06-17

## FengWu技术细节 (论文: arXiv:2304.02948)

FengWu是基于人工智能的全球中期气象预报系统，发表于Nature Communications Earth & Environment (2025)。

### 模型架构
- 采用多模态多任务深度学习架构
- 配备模型特定编解码器(model-specific encoder-decoders)和跨模态融合Transformer(cross-modal fusion Transformer)
- 使用不确定性损失(uncertainty loss)在不同预测因子间进行区域自适应优化

### 训练数据
- 基于39年ERA5再分析数据(1979-2017)训练
- 0.25度经纬度分辨率，37个垂直气压层
- 引入replay buffer机制改善中期预报性能

### 评测结果
- 在880个预报因子中80%优于GraphCast
- 10天z500预报RMSE从733降至651 m2/s2(vs GraphCast)
- 首次将有效预报时效延伸至10.75天(z500 ACC > 0.6)
- 单次推理仅需600毫秒(NVIDIA Tesla A100)

### 技术栈
- 推理硬件: NVIDIA Tesla A100
- 预报步长: 6小时
- 输出: 37个垂直层的大气和地面状态预测