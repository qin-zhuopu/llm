# Sourcegraph — Code Understanding, Oversight and Evolution (Amp)

Source: https://sourcegraph.com
Fetched: 2026-08-27

Take control of your codebase. Give humans and agents complete context to understand, oversee, and evolve the world's largest, most complex codebases. Trusted by 200+ enterprise engineering teams.

## The problem
A tidal wave of code is coming. Code is growing faster than teams can understand or control it. Agents see only fragments of the enterprise codebase, rebuilding context for each task. As agent adoption grows, that blind spot becomes inconsistency, missed changes, and risk at scale.

## The solution
Take back control with complete codebase context. Sourcegraph indexes all repositories across the entire codebase, empowering agents with full context. Example: a cross-cutting change to add a Role field to a User struct — a naive agent misses auth middleware, API response DTO, audit logging, frontend routes, invite flow, integration tests; Sourcegraph found 31 files referencing User across 7 layers and edited 12 files across 7 layers with nothing missed.

- Code understanding: agents get full codebase intelligence.
- Code oversight: understand system-wide impact before changes ship; track patterns, monitor risk.
- "Minions are connected to MCP… this is how they gather context: internal docs, ticket details, build statuses, and code intelligence via Sourcegraph search."

## Security & scale
- SOC2 Type II + ISO27001 Compliance.
- Zero data retention: LLM inference never stored beyond what's required and never shared with third parties.
- Built to scale: handles the world's largest monorepos and multi-repo architectures.
- Enterprise authentication: SSO (SAML, OpenID Connect, OAuth), SCIM provisioning, RBAC.

## CodeScaleBench Report
Sourcegraph makes agents faster, cheaper, and more accurate: cost/task ▼30%, exec speed ▲38%, retrieval ▲2–3×.

Amp is Sourcegraph's agentic coding tool that leverages this codebase context.
