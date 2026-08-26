# 垂直业务领域闭源大语言模型调研

> 聚焦于垂直业务领域的闭源大语言模型汇总，不包含聚焦于AI技术本身（如通用编程、代码生成）的模型。

## 领域分类

### Tier 1 — 成熟度最高、模型最密集

| # | 领域 | 说明 |
|---|------|------|
| 1 | [金融](domains/finance/) | 银行、证券、保险、投研、风控、合规 |
| 2 | [医疗健康](domains/healthcare/) | 临床辅助、医学影像、健康管理、医疗问答 |
| 3 | [法律](domains/legal/) | 合同审查、法律研究、诉讼支持、合规 |

### Tier 2 — 快速增长、多家厂商布局

| # | 领域 | 说明 |
|---|------|------|
| 4 | [电商零售](domains/retail-ecommerce/) | 客服、选品、商品文案、供应链、推荐 |
| 5 | [教育](domains/education/) | K12辅导、自适应学习、语言教学、学术辅助 |
| 6 | [汽车出行](domains/automotive/) | 自动驾驶决策、座舱交互、交通规划 |
| 7 | [药物研发](domains/pharma-biotech/) | 靶点发现、分子生成、临床试验优化 |
| 8 | [工业制造](domains/manufacturing/) | 工业自动化、预测性维护、质量检测、PLC编程 |

### Tier 3 — 有明确场景、已有产品落地

| # | 领域 | 说明 |
|---|------|------|
| 9 | [电信](domains/telecom/) | 网络运维、故障预测、客服、资源调度 |
| 10 | [能源](domains/energy/) | 电力调度、油气勘探、碳排管理、新能源预测 |
| 11 | [政务](domains/government/) | 政务问答、公文写作、舆情分析、城市大脑 |
| 12 | [建筑地产](domains/construction-realestate/) | 建筑设计、BIM协同、造价估算、合规审查 |
| 13 | [媒体娱乐](domains/media-entertainment/) | 内容生产、剧本创作、游戏NPC、新闻摘要 |
| 14 | [物流供应链](domains/logistics-supplychain/) | 路线优化、仓储管理、需求预测、调度 |

### Tier 4 — 新兴/利基、探索阶段

| # | 领域 | 说明 |
|---|------|------|
| 15 | [农业](domains/agriculture/) | 病虫害诊断、种植方案、产量预测、农机调度 |
| 16 | [材料科学](domains/materials-science/) | 新材料发现、材料性能预测、配方优化 |
| 17 | [气象环保](domains/climate-environment/) | 天气预报、气候建模、环境监测、灾害预警 |
| 18 | [航空航天与国防](domains/aerospace-defense/) | 航路规划、卫星遥感、情报分析、装备维护 |
| 19 | [人力资源](domains/human-resources/) | 简历筛选、人岗匹配、培训内容生成 |
| 20 | [会计审计](domains/accounting-audit/) | 财务审计、税务合规、报表分析 |

## AI 平台

除垂直领域模型外，本仓库还收录提供推理API和训练API的AI平台：

| # | 平台 | 公司 | 推理API | 训练API | 说明 |
|---|------|------|---------|---------|------|
| 1 | [Tinker](platforms/tinker.yaml) | Thinking Machines Lab | Beta (Inkling系列) | GA (28+模型LoRA) | 前OpenAI CTO Mira Murati创立，$2B融资 |

平台数据结构参见 [`platforms/schema.json`](platforms/schema.json)，推理API为必填字段。

---

## Tier 分级依据

- 已公开的专用闭源模型数量
- 市场报告中的投资规模和增速（参考 Precedence Research、MarketsandMarkets）
- 头部厂商布局密度
- NVIDIA 行业 AI 报告中的行业成熟度

## 数据来源

- [Precedence Research - Large Language Model Market](https://www.precedenceresearch.com/large-language-model-market)
- [Sequoia Capital - Generative AI's Act Two](https://www.sequoiacap.com/article/generative-ai-act-two/)
- [NVIDIA Industries](https://www.nvidia.com/en-us/industries/)
- 各公司官网及 arXiv 论文

## 分类逻辑

1. **排除了"AI技术本身"类**：如代码生成（Copilot类）、AI基础设施、通用对话等
2. **合并了过细的子类**：如"银行"和"保险"合并到"金融"
3. **"药物研发"从"医疗"独立**：面向的用户（药企 vs 医院）、数据形态（分子 vs 病历）、商业模式完全不同

## 开发

### 安装依赖

```bash
pip install -r requirements.txt
```

### 验证所有模型文件

```bash
python scripts/validate.py
```

### 添加新模型

1. 在对应领域文件夹下创建 `{模型名}.yaml`
2. 按照 `schema/model.schema.json` 的格式填写字段
3. 运行 `python scripts/validate.py` 确认无格式错误
4. 提交 PR

### 添加新平台

1. 在 `platforms/` 文件夹下创建 `{平台名}.yaml` 和 `{平台名}.md`
2. 按照 `platforms/schema.json` 的格式填写字段（推理API为必填）
3. 运行 `python scripts/validate_platforms.py` 确认无格式错误
4. 提交 PR
