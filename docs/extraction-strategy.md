# 提取策略 (Extraction Strategy)

## 提取架构

```
orchestrator (编排器)
  → subagent_coder (子代理/编码代理)
    → scripts/extract_yaml.py (提取脚本)
      → LLM API (glm-4.5-air / glm-5.3)
```

- **orchestrator**: 负责任务规划和子代理调度
- **subagent_coder**: 执行具体的提取任务，拥有文件读写工具
- **extract_yaml.py**: 核心提取脚本，读取 md 文件，构建 prompt，调用 LLM API，生成 YAML
- **LLM API**: 大模型接口，解析非结构化文本输出结构化数据

## 截断策略

**禁止任何形式的截断。**

- 当前项目中最大的 md 文件约 24,069 chars (~8K tokens)
- 模型上下文窗口: glm-4.5-air 128K tokens, glm-5.3 128K+ tokens
- 即使最大文件，输入 prompt 总量也远低于模型上下文限制
- 截断会丢失关键信息（如 benchmark 数据通常在文档后半部分），严重影响提取质量

历史教训：
- harvey-lab-agent.md (18,076 chars) 被截断 55%，大量技术细节丢失
- harvey-review-table.md (12,670 chars) 被截断 37%，所有 benchmark 数据在截断点之后

## 子代理策略

当 orchestrator 委派提取任务给子代理时：

1. **不要在 orchestrator 的 prompt 里嵌入 md 原文**
2. **只嵌入相关 md 文件的路径**（如 `domains/legal/harvey-lab-agent.md`）
3. **让子代理自己使用 read_file 工具读取文件内容**

原因：
- 子代理拥有 read_file 等文件操作工具，可以自主读取任何文件
- 将大段 md 内容嵌入 orchestrator 的 prompt 会浪费 token 配额
- 文件路径传递更简洁、更可靠

注意：`extract_yaml.py` 脚本本身是直接调用 LLM API 的（不是通过子代理），
因此脚本内部必须将完整 md 内容嵌入到发送给 LLM 的 prompt 中。

## LLM 选择

| 模型 | 上下文窗口 | 用途 | 备注 |
|------|-----------|------|------|
| glm-4.5-air | 128K tokens | 默认提取模型 | 速度快、成本低 |
| glm-5.3 | 128K+ tokens | 可选高质量模型 | 复杂提取场景 |

配置方式（环境变量）：
```bash
export ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
export ANTHROPIC_AUTH_TOKEN=<your-token>
export ANTHROPIC_MODEL=glm-4.5-air  # 或 glm-5.3
```

## 日志要求

每次提取必须输出以下日志信息：

1. **模型名**: 使用的 LLM 模型标识
2. **输入大小**: MD 文件原始大小 (chars)，Prompt 总大小 (chars)，估算 tokens (chars/3)
3. **输出大小**: 实际输入/输出 tokens（从 API 响应的 usage 字段获取）
4. **提取字段**: 成功提取的 YAML 字段列表

示例输出：
```
    📊 模型: glm-4.5-air
    📊 MD 文件大小: 18076 chars
    📊 Prompt 大小: 22534 chars (~7511 tokens 估算)
    📊 实际输入 tokens: 8234, 输出 tokens: 1567
```

## 质量检查

提取完成后，应运行质量检查验证提取结果：

```bash
python scripts/check.py --details domains/legal/harvey-lab-agent.yaml
```

check.py 评估三个维度：
1. **completeness** (完整度): 填写了多少可选字段
2. **richness** (丰富度): description 长度、capabilities 数量等
3. **confidence** (置信度): 基于来源可靠性的综合评分

目标：每个 YAML 文件的综合得分应达到 7/10 以上。
