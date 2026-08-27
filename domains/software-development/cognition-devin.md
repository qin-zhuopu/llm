---
title: Devin (Cognition AI) — 自主 AI 软件工程师
date: 2026-08-27
source: https://cognition.ai/blog/introducing-devin
---

# Devin (Cognition AI) — 首个 AI 软件工程师

> 来源: https://cognition.ai/blog/introducing-devin ，https://cognition.ai/blog/swe-bench-technical-report ，https://en.wikipedia.org/wiki/Cognition_AI
> 抓取日期: 2026-08-27

Devin 是 Cognition AI 开发的自主 AI 软件工程师，定位为可独立端到端完成工程任务的 AI 队友。它于 2024 年 3 月首次发布 demo，是"自主软件工程师（autonomous software engineer）"这一品类的开创者。

## 核心能力（官网）
- **长期推理与规划**：可规划并执行需要数千次决策的复杂工程任务，在每一步召回相关上下文、随时间学习、修复错误。
- **完整开发者工具**：在沙箱化的计算环境中配备 shell、代码编辑器和浏览器——人类完成工作所需的一切。
- **主动协作**：实时汇报进度、接受反馈、与用户一起做设计决策。
- 示例：读博客后学会用 ControlNet；端到端构建并部署应用（Game of Life → Netlify）；自主发现并修复 bug；给定 GitHub issue 链接自主完成 setup 与上下文收集；在 SWE-bench 中修复 sympy 的对数计算 bug；甚至在 Upwork 上完成真实工作。

## 性能（SWE-bench 技术报告）
- 在 SWE-bench（2,294 个真实 GitHub issues + PRs 数据集，通过单元测试确定性评估）上，Devin 在**无辅助（unassisted）**设定下解决 **13.86%** 的问题，远超此前无辅助 SOTA 的 1.96%；即使给出精确待改文件（assisted），此前最佳模型也仅解决 4.80%。
- 方法学：标准化 prompt 仅给 issue 描述；克隆仓库仅保留 base commit 及祖先防泄漏、移除 git remote；限制 Devin 运行 45 分钟。
- 结果：在随机抽取的 25%（570/2294）测试集上，解决 79/570 = 13.86%。评估 harness 与 Devin 编辑结果开源于 github.com/CognitionAI/devin-swebench-results。

## 架构定位
Devin 属于**模型系统型/工作流应用型**混合：Cognition 是"专注推理的应用 AI 实验室"，Devin 是在前沿基座模型之上构建的自主 Agent 系统（长期规划、工具使用、沙箱执行、自我修复），并非公开的单一垂类基础模型。

## 商业数据（Wikipedia / 媒体）
- 2023 年 8 月由 Scott Wu（CEO）、Steven Hao（CTO）、Walden Yan（CPO）创立，三人均获 IOI 金牌。约 200 名员工（2026）。
- 产品：Devin AI、DeepWiki、Devin Desktop。
- 融资/估值：Founders Fund $21M 种子轮（$350M 估值）→ 2024/04 $175M（$2B，独角兽）→ 2025/03 $4B（8VC 领投）→ 收购 Windsurf 后 2025/09 达 $10B → 2026/05 达 $26B；2026/08 Bloomberg 报道正洽谈 ≥$40B 估值新融资。
- 2025/07 收购 Windsurf（agentic IDE），2026/06 更名为 Devin Desktop。
