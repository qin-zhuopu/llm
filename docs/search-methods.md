# 搜索方法和数据源

## 搜索方法枚举

| 编号 | 方法 | 说明 | 适用场景 |
|------|------|------|---------|
| `api-catalog` | 平台 API 目录抓取 | 直接调用平台 API 获取结构化模型列表 | 通用模型聚合器 |
| `official-website` | 公司官网采集 | 直接从产品/公司官网抓取内容 | 已知目标公司 |
| `github-awesome` | GitHub Awesome 列表 | 从 Awesome-X 类项目获取领域模型列表 | 领域全景扫描 |
| `industry-report` | 行业报告/投资报告 | 从 Sequoia/CB Insights 等机构获取行业地图 | 发现新公司 |
| `snowball` | 顺藤摸瓜 | 从已知公司的竞争对手/合作伙伴/同领域延伸 | 深入特定领域 |
| `web-search` | 通用网络搜索 | 用关键词搜索发现新目标 | 初始探索 |
| `paper-trace` | 论文追踪 | 从 arXiv/Nature 论文反向找到公司/产品 | 学术→商业 |

## 搜索平台枚举

| 编号 | 平台 | URL | 类型 | 发现垂直模型？ |
|------|------|-----|------|:---:|
| `hf-inference` | HuggingFace Inference Providers | router.huggingface.co/v1/models | API 目录 | ❌ (131 通用) |
| `openrouter` | OpenRouter | openrouter.ai/models | API 目录 | ❌ (400+ 通用) |
| `models-dev` | Models.dev | models.dev | 数据库 | ❌ (250+ 通用) |
| `together` | Together AI | docs.together.ai/docs/serverless-models | API 目录 | ❌ (通用) |
| `aws-bedrock` | AWS Bedrock | aws.amazon.com/bedrock | 云平台 | ❌ (通用+定制) |
| `nvidia-ngc` | NVIDIA NGC/NIM | catalog.ngc.nvidia.com | 工具库 | 🔸 (BioNeMo) |
| `gh-awesome-domain` | Awesome-Domain-LLM | github.com/luban-agi/Awesome-Domain-LLM | GitHub | ✅ (50+ 开源) |
| `gh-fingpt` | FinGPT | github.com/AI4Finance-Foundation/FinGPT | GitHub | ✅ (金融开源) |
| `gh-open-llms` | Open LLMs | github.com/eugeneyan/open-llms | GitHub | ❌ (通用) |
| `gh-awesome-ai-tools` | Awesome AI Tools | github.com/mahseema/awesome-ai-tools | GitHub | ❌ (通用工具) |
| `sequoia` | Sequoia Capital 报告 | sequoiacap.com | 投资报告 | ✅ (Harvey 等) |
| `cb-insights` | CB Insights AI 100 | cbinsights.com | 投资报告 | ✅ (付费) |
| `john-snow-labs` | John Snow Labs | johnsnowlabs.com | 垂直平台 | ✅ (医疗 NLP) |
| `direct-search` | 直接搜索公司官网 | 各公司 | 官网 | ✅ |

## 每个模型的发现来源

### 能源
| 模型 | 方法 | 来源平台 | 发现路径 |
|------|------|---------|---------|
| Baker Hughes AI | web-search | 官网 | 初始调研 |
| 国网智能电网AI | web-search | 官网 | 初始调研 |
| Gridmatic | snowball | gridmatic.com | 从"能源AI"关键词搜索发现 |

### 农业
| 模型 | 方法 | 来源平台 | 发现路径 |
|------|------|---------|---------|
| 丰农AI | web-search | 官网 | 初始调研 |
| XAG AI | web-search | 官网 | 初始调研 |
| Taranis | snowball | taranis.com | 从"农业AI"搜索+Syngenta合作新闻 |
| Indigo Ag | snowball | indigo-ag.com | 从农业AI公司延伸 |

### 金融
| 模型 | 方法 | 来源平台 | 发现路径 |
|------|------|---------|---------|
| BloombergGPT | paper-trace | arxiv.org | 论文 arXiv:2303.17564 |
| 蚂蚁百灵 | web-search | antgroup.com | 初始调研 |
| Goldman Sachs AI | web-search | 官网 | 初始调研 |
| Shift Technology | snowball | shift-technology.com | 从"保险AI"搜索 |
| Tractable | snowball | tractable.ai | 从"保险理赔AI"搜索 |
| CAPE Analytics | snowball | capeanalytics.com | 从保险AI延伸 |

### 医疗
| 模型 | 方法 | 来源平台 | 发现路径 |
|------|------|---------|---------|
| Med-PaLM 2 | paper-trace | Google | 论文+官方博客 |
| 华佗GPT | gh-awesome-domain | GitHub | Awesome-Domain-LLM |
| Hippocratic AI | web-search | 官网 | 初始调研 |
| Abridge | direct-search | abridge.com | "临床AI"关键词搜索 |
| Nabla | snowball | nabla.com | 从Abridge竞品延伸 |
| PathAI | snowball | pathai.com | 从医疗AI公司延伸 |

### 法律
| 模型 | 方法 | 来源平台 | 发现路径 |
|------|------|---------|---------|
| Harvey AI | industry-report | Sequoia报告 | "Act Two"文章提及 |
| CoCounsel | web-search | casetext.com | 初始调研 |
| Relativity aiR | direct-search | relativity.com | "法律AI"搜索 |

### 材料科学
| 模型 | 方法 | 来源平台 | 发现路径 |
|------|------|---------|---------|
| DeepMind GNoME | paper-trace | Nature | 论文 |
| Microsoft MatterGen | paper-trace + snowball | Microsoft Research Blog | 用户提示→MS Research博客 |
| Meta OCP | snowball | opencatalystproject.org | 用户提示→OCP官网 |
| Orbital Materials | snowball | orbitalmaterials.com | 从MatterGen竞品搜索 |
| Kebotix | snowball | kebotix.com | 从"self-driving lab"关键词延伸 |
| Aionics | snowball | aionics.io | 从"电池材料AI"延伸 |
| Atinary | snowball | atinary.com | 从"self-driving lab"延伸 |
| Chemify | snowball | chemify.io | 从材料科学AI公司列表延伸 |
| Citrine | web-search | citrine.io | 初始调研 |

### 药物研发
| 模型 | 方法 | 来源平台 | 发现路径 |
|------|------|---------|---------|
| NVIDIA BioNeMo | nvidia-ngc | nvidia.com | NGC平台 |
| Recursion | web-search | recursion.com | 初始调研 |
| 晶泰科技 | web-search | xtalpi.com | 初始调研 |
| Iambic Therapeutics | snowball | iambic.ai | 从"AI药物发现"延伸 |
| Deep Origin | snowball | deeporigin.com | 从Iambic竞品延伸 |

## 搜索效率分析

| 方法 | 发现模型数 | 命中率 | 最适合 |
|------|-----------|--------|--------|
| `snowball` | ~25 | 高 | 深入特定领域、发现竞品 |
| `web-search` | ~20 | 中 | 初始探索、已知公司 |
| `paper-trace` | ~8 | 高 | 有学术论文的模型 |
| `api-catalog` | 0 | ❌ | 只适合通用模型 |
| `gh-awesome-domain` | ~5 (开源) | 中 | 开源模型、评测基准 |
| `industry-report` | ~3 | 低(付费) | 发现行业地图 |
| `direct-search` | ~5 | 高 | 已知目标 |

## 尚未充分探索的渠道

- Crunchbase / PitchBook 投资数据库（付费）
- Product Hunt AI 分类
- G2/Gartner 行业报告
- 中国：36氪/量子位/机器之心 AI 报道
- 日本/韩国本地 AI 公司
- 中东（阿联酋 G42/沙特 SDAIA）
