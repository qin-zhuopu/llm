# 原始资料目录 (Raw Materials)

本目录用于存储每个模型研究过程中获取的原始内容，作为 `.md` 摘要文件的证据来源。

## 目录结构

```
data/raw/
├── README.md                    # 本文件
├── {model-slug}/                # 每个模型一个文件夹，slug 与 domains/ 下的文件名一致
│   ├── sources.json             # 来源记录文件（必需）
│   ├── github-readme.md         # GitHub README 原始内容
│   ├── arxiv-abstract.txt       # arXiv 论文摘要
│   ├── official-website.md      # 官网抓取内容
│   └── ...                      # 其他原始资料文件
```

## sources.json 格式

每个模型文件夹下必须包含 `sources.json`，记录所有原始文件的来源信息：

```json
{
  "files": [
    {
      "filename": "github-readme.md",
      "url": "https://github.com/PKU-YuanGroup/ChatLaw",
      "fetched_at": "2025-06-17",
      "type": "github"
    },
    {
      "filename": "arxiv-abstract.txt",
      "url": "https://arxiv.org/abs/2306.16092",
      "fetched_at": "2025-06-17",
      "type": "arxiv"
    }
  ]
}
```

### 字段说明

| 字段 | 说明 |
|------|------|
| `filename` | 本地保存的文件名 |
| `url` | 原始来源 URL |
| `fetched_at` | 抓取日期（YYYY-MM-DD 格式） |
| `type` | 来源类型：`github`, `arxiv`, `official-website`, `blog`, `huggingface`, `paper-pdf` 等 |

## 文件命名规范

| 来源类型 | 推荐文件名 |
|----------|-----------|
| GitHub README | `github-readme.md` |
| arXiv 论文页 | `arxiv-abstract.txt` |
| 官方网站 | `official-website.md` |
| 技术博客 | `blog-{slug}.md` |
| Hugging Face 模型卡 | `huggingface-model-card.md` |
| 其他 | 使用描述性名称，小写，连字符分隔 |

## 使用流程

1. 子代理通过 `web_fetch` 获取原始内容
2. 将内容保存到 `data/raw/{model-slug}/{filename}`
3. 在 `sources.json` 中添加对应记录
4. 基于原始内容整理摘要，写入 `domains/{category}/{model-slug}.md`

## 与 md 文件的关系

- `domains/` 下的 `.md` 文件是整理后的摘要
- `data/raw/` 下的文件是原始证据
- md 文件中标注的来源 URL 应与 `sources.json` 中的记录一致
- 如需验证 md 中的信息，可回溯到 raw 文件查看原始上下文
