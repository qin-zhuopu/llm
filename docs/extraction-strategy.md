# 提取策略 (Extraction Strategy)

> 本文档记录项目提取架构的完整演进过程和最终策略。

## 1. 提取架构（最终版）

### 两种模式对比

| | 旧模式（已弃用） | 新模式（当前） |
|---|---|---|
| 流程 | orchestrator → subagent → extract_yaml.py → glm-4.5-air API | orchestrator → subagent（直接读 md + schema，自己理解内容，自己写 YAML） |
| 状态 | ❌ 弃用 | ✅ 正式采用 |

### 为什么新模式更好

1. **子代理本身就是大模型，能力远强于 glm-4.5-air**
   - 子代理可以进行多步推理、交叉验证信息、推断缺失字段、保持字段间一致性
   - glm-4.5-air 只能做单轮文本到 YAML 的映射

2. **不经过脚本中间层，没有截断、格式转换等信息损失**
   - 旧脚本会截断输入、限制输出 token、丢弃上下文
   - 子代理直接访问完整文件内容

3. **子代理可以自主研究补充信息**
   - 遇到 md 文件信息不足时，可以主动用 web_fetch 访问外部来源
   - glm-4.5-air 只能基于传入的文本生成结果

## 2. 截断策略

**禁止任何形式的截断。**

### 历史教训（具体数据）

旧脚本使用 8000 字符截断限制，而模型上下文窗口为 128K tokens：

- 8000 chars ≈ 2700 tokens，仅占模型上下文的 **2-6%**
- `harvey-lab-agent.md` (18,076 chars) 被截断 **55%**，大量技术细节丢失
- `harvey-review-table.md` (12,670 chars) 所有 benchmark 数据位于截断点之后，完全丢失

### 实际需求

- 项目中最大的 md 文件约 24K chars (~8K tokens)
- 模型上下文窗口 128K tokens
- 即使加上 schema prompt 和系统指令，总输入远低于上下文限制
- **完全不需要截断**

## 3. 子代理策略

orchestrator 传递任务时的规则：

1. **只传文件路径列表**，不嵌入 md 原文
2. **子代理自己用 `read_file` 读取** md 文件内容
3. **子代理自己用 `web_fetch` 补充**不足的信息

原因：
- 将大段 md 内容嵌入 orchestrator 的 prompt 会浪费 token 配额
- 子代理拥有完整的文件操作工具，可以自主读取任何文件
- 文件路径传递更简洁、更可靠、更灵活

## 4. 自主研究流程（关键新增）

子代理的完整工作流：

```
1. 读 schema/model.schema.json 了解字段定义
2. 读 .md 文件，评估信息充分度
3. 如果 md 信息不足以填充 training/benchmarks/tech_stack：
   - 用 web_fetch 访问公司官网、产品页
   - 搜索 arXiv 论文、GitHub README
   - 查找技术博客和发布公告
4. 将新发现追加到 .md 文件（用 `---` 分隔，标注来源 URL 和日期）
5. 基于完整信息写 .yaml
6. 运行 validate.py 确认 schema 通过
```

### 信息补充规范

当子代理通过 web_fetch 获取到新信息时，追加到 md 文件末尾：

```markdown
---

## 补充信息

> 来源: https://example.com/blog/model-release
> 获取日期: 2025-06-17

（补充内容...）
```

### 适合自主研究的字段

| 字段 | 典型来源 |
|------|---------|
| training.method | 论文、技术博客 |
| training.data_sources | 论文、GitHub README |
| benchmarks | 论文、模型卡片、排行榜 |
| tech_stack | GitHub repo、文档 |
| parameters | 模型卡片、Hugging Face |

## 5. 质量指标

### 评分系统

`check.py` 三维度打分：

- **业务 (B)**: description, capabilities, access, website, references
- **技术 (T)**: parameters, architecture, base_model, training, tech_stack, datasets, benchmarks
- **来源 (S)**: md 文件大小, 具体数据点, 论文引用, 官方来源

### 项目质量变化记录

| 阶段 | 综合 | B (业务) | T (技术) | S (来源) | 说明 |
|------|------|----------|----------|----------|------|
| 初始 | **48** | 86 | 5 | 53 | extract_yaml.py + glm-4.5-air + 8000 char 截断 |
| 第二阶段 | **64** | 90 | 47 | 53 | 去掉截断 + 子代理直接提取 |
| 第三阶段 | **79** | 94 | 77 | 67 | 子代理自主搜索补充 |

### 关键提升分析

- 初始 → 第二阶段（+16分）：去掉截断后技术字段从 5 提升到 47，信息不再丢失
- 第二阶段 → 第三阶段（+15分）：自主研究让技术字段从 47 提升到 77，来源从 53 提升到 67

## 6. extract_yaml.py 脚本的定位

脚本仍然保留，但**不再是主要提取手段**。

### 适用场景

- 批量初始化：大量新 md 文件需要快速生成 YAML 草稿
- 低优先级模型：对质量要求不高的场景

### 已修复的问题

- ✅ 去掉 8000 字符截断限制
- ✅ max_tokens 提升到 8192
- ✅ 添加详细日志输出（模型名、输入大小、输出 tokens）

### 使用建议

| 场景 | 推荐方式 |
|------|---------|
| 需要高质量结果 | 子代理直接提取 + 自主研究 |
| 批量初始化草稿 | extract_yaml.py |
| 单个模型精细提取 | 子代理直接提取 |

## 7. 批处理策略

- 子代理每批处理 **10-15 个模型**
- 太多会导致上下文过长、质量下降
- 每批结束后运行 `validate.py` + `test_all.py` 确认

### 批处理流程

```
1. orchestrator 选出 10-15 个待处理模型
2. 传递路径列表给子代理
3. 子代理逐个处理：读 md → (可选) web_fetch → 写 yaml
4. 子代理运行 validate.py 确认所有 yaml 通过 schema 校验
5. 子代理运行 test_all.py 确认无回归
6. 提交本批结果
```

### 注意事项

- 如果某个模型的 web_fetch 失败或超时，跳过自主研究，仅基于现有 md 提取
- 每批处理完后检查 check.py 分数，确认质量符合预期
- 优先处理低分模型（按 check.py 综合分排序）
