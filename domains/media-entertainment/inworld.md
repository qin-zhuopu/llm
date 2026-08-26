# Inworld AI — 面向消费级应用的实时 AI（游戏/实时语音）

> 来源: https://inworld.ai
> 抓取日期: 2026-08-26

Inworld AI 是面向消费级应用的实时 AI 平台，为大规模语音优先的伴侣类应用提供支持，实现持续、个性化、情感投入的 AI 交互。

## 核心产品

### Realtime TTS（实时语音合成）
自然的实时文本转语音。Realtime TTS-2 首字延迟 <100ms，TTS-2 Flash 25ms。语音 Agent 在用户察觉延迟之前就能响应。

### Realtime API（实时语音对语音）
可控的 speech-to-speech，通过单个 WebSocket 实现语音输入/输出，支持自定义语音和工具调用。全双工低延迟流、智能轮次检测、会话中注册工具、provider 无关路由、动态上下文管理、对话智能。

### Realtime Router（实时路由）
一个 API 智能路由到 OpenAI、Anthropic、Google 和 220+ 模型。零加价（zero markup），只付 provider 费率。内置分析、故障转移、A/B 测试和智能模型选择。热门模型：Gemini 3 Flash (16%)、Qwen3 Max (14%)、Claude Sonnet 4.6 (12%)。

### Realtime STT（实时语音识别）
带内置语音画像的 speech-to-text，实时流低至 $0.10/小时。内置语音画像（情绪、年龄、口音、音高、风格）、语义/声学 VAD、词级时间戳和说话人分离。

## 激进定价（补贴 AI 成本让消费应用可规模化）

- Realtime TTS：$12.50 vs ElevenLabs $100 / 1M 字符
- Realtime STT：$0.10 vs Deepgram $0.46 / 小时
- LLM 加价：0% vs 典型网关 5%
- 专用 GPU：$5 vs 超大规模云商 $10+ / GPU-小时

## 规模

Status 应用 19 天达到 100 万用户；数百万开发者使用。

## 合规

SOC2 Type II、HIPAA、GDPR 认证，基于零信任框架。

## 定位（据行业报告）

Inworld 在垂类 AI 竞争格局中属于"实时体验型"（游戏/实时语音）。技术核心不只是准确率，还包括延迟、语音质量、对话连续性、安全边界和推理成本——"推理经济学 + 体验工程"本身就是壁垒。已从垂直（游戏 NPC）向通用语音基础设施扩张，需关注平台化后的差异化。
