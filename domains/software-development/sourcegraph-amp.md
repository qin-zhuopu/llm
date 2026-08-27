---
title: Sourcegraph Amp — 代码库上下文驱动的自主编码 Agent
date: 2026-08-27
source: https://sourcegraph.com
---

# Sourcegraph Amp — 代码库上下文驱动的编码 Agent

> 来源: https://sourcegraph.com ，https://ampcode.com
> 抓取日期: 2026-08-27（ampcode.com 抓取时返回 header overflow，产品描述据 sourcegraph.com 官方页面整理）

Amp 是 Sourcegraph 推出的自主编码 Agent。Sourcegraph 的核心是**代码理解/代码智能平台**，索引企业全部代码仓库，为人类和 Agent 提供完整代码库上下文。属于**模型系统型/工作流应用型**：不自研通用基础模型，而是以自研的**检索/上下文引擎（context engine）**为核心，编排前沿模型完成跨文件、跨层的复杂改动。

## 核心命题
- "Agents are only as good as the context they receive."（Agent 的好坏取决于它得到的上下文）
- 问题：Agent 只能看到企业代码库的碎片，每个任务都要重建上下文，随规模扩大形成盲区、导致不一致与遗漏。
- 解决：Sourcegraph 索引所有仓库，给 Agent 完整上下文。示例——给 User 结构体加 Role 字段这类跨层改动，朴素 Agent 会漏掉鉴权中间件、API DTO、审计日志、前端路由、邀请流程、集成测试；Sourcegraph 找到跨 7 层 31 个引用 User 的文件，改动 12 个文件"nothing missed"。

## 平台能力
- **Code understanding**：给 Agent 完整代码库智能。
- **Code oversight**：在改动上线前理解系统级影响，追踪模式、监控风险。
- Minions 通过 MCP 连接，收集内部文档、工单细节、构建状态，并通过 Sourcegraph search 获取代码智能。

## 企业级与规模
- SOC2 Type II + ISO27001 合规；零数据保留（LLM 推理不留存、不与第三方共享）。
- 处理世界最大 monorepo 与多仓架构；SSO（SAML/OIDC/OAuth）、SCIM、RBAC。
- 服务 200+ 企业工程团队。
- **CodeScaleBench**：Sourcegraph 让 Agent 更快更省更准——cost/task ▼30%、执行速度 ▲38%、检索 ▲2–3×。

## 定位
模型系统型：核心资产是代码检索/上下文引擎，Amp 在其上编排前沿模型，护城河是"大规模代码库的完整上下文"。
