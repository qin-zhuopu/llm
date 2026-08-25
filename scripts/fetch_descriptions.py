#!/usr/bin/env python3
"""从每个模型的官网抓取描述信息，保存为同目录下的 .md 文件。

用法:
    python3 scripts/fetch_descriptions.py              # 抓取所有缺少 .md 的模型
    python3 scripts/fetch_descriptions.py --force      # 强制重新抓取所有
    python3 scripts/fetch_descriptions.py --domain finance  # 只抓某个领域
    python3 scripts/fetch_descriptions.py --file domains/legal/harvey-ai.yaml  # 只抓单个
"""

import argparse
import sys
import time
import traceback
from pathlib import Path
from datetime import datetime

import requests
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify as md


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

TIMEOUT = 30  # 秒
DELAY = 2  # 请求间隔（秒），避免被封


def fetch_and_convert(url: str):
    """抓取 URL 并转换为 markdown 格式。"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        resp.raise_for_status()
    except requests.RequestException as e:
        return None, str(e)

    # 解析 HTML
    soup = BeautifulSoup(resp.text, "html.parser")

    # 移除不需要的元素
    for tag in soup.find_all(["script", "style", "nav", "footer", "header", "noscript", "iframe"]):
        tag.decompose()

    # 尝试找到主要内容区域
    main_content = (
        soup.find("main")
        or soup.find("article")
        or soup.find(attrs={"role": "main"})
        or soup.find("div", class_=lambda c: c and ("content" in c.lower() or "main" in c.lower()))
        or soup.find("body")
    )

    if main_content is None:
        main_content = soup

    # 移除图片标签（无法保存）
    for img in main_content.find_all("img"):
        img.decompose()

    # 转换为 markdown
    content = md(
        str(main_content),
        heading_style="ATX",
        strip=["button", "form", "input", "select", "svg"],
    )

    # 清理多余空行
    lines = content.split("\n")
    cleaned = []
    prev_empty = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if not prev_empty:
                cleaned.append("")
            prev_empty = True
        else:
            cleaned.append(line)
            prev_empty = False

    return "\n".join(cleaned).strip(), None


def process_model(yaml_path: Path, root: Path, force: bool = False):
    """处理单个模型文件，返回 (状态, 消息)。"""
    md_path = yaml_path.with_suffix(".md")
    relative = yaml_path.relative_to(root)

    # 如果 .md 已存在且非强制模式，跳过
    if md_path.exists() and not force:
        return "skip", f"{relative} → 已存在，跳过"

    # 读取 YAML
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not data:
        return "error", f"{relative} → YAML 为空"

    url = data.get("website")
    if not url:
        return "error", f"{relative} → 无 website 字段"

    name = data.get("name", yaml_path.stem)
    company = data.get("company", "")

    # 抓取
    content, error = fetch_and_convert(url)

    if error:
        return "error", f"{relative} → 抓取失败: {error}"

    if not content or len(content.strip()) < 50:
        return "error", f"{relative} → 内容过短或为空"

    # 生成 markdown 文件
    header = f"""# {name}

> 来源: [{url}]({url})
> 抓取时间: {datetime.now().strftime("%Y-%m-%d")}
> 公司: {company}

---

"""
    full_content = header + content

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_content)

    size = len(full_content)
    return "ok", f"{relative} → 保存为 {md_path.name} ({size:,} 字符)"


def main():
    parser = argparse.ArgumentParser(description="抓取模型官网描述保存为 markdown")
    parser.add_argument("--force", action="store_true", help="强制重新抓取已存在的文件")
    parser.add_argument("--domain", type=str, help="只抓取指定领域")
    parser.add_argument("--file", type=str, help="只抓取单个 YAML 文件")
    parser.add_argument("--dry-run", action="store_true", help="只显示要抓取的列表，不实际抓取")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    domains_path = root / "domains"

    # 收集要处理的文件
    if args.file:
        target = Path(args.file)
        if not target.is_absolute():
            target = root / target
        model_files = [target]
    else:
        yaml_files = sorted(domains_path.rglob("*.yaml"))
        model_files = [f for f in yaml_files if f.name != "_meta.yaml"]
        if args.domain:
            model_files = [f for f in model_files if f.parent.name == args.domain]

    if not model_files:
        print("❌ 未找到匹配的模型文件")
        sys.exit(1)

    print(f"📥 模型官网描述抓取工具")
    print(f"   目标文件: {len(model_files)} 个")
    print(f"   模式: {'强制重抓' if args.force else '增量（跳过已有）'}")
    print(f"{'=' * 60}")

    if args.dry_run:
        for f in model_files:
            data = yaml.safe_load(open(f, encoding="utf-8"))
            url = data.get("website", "N/A") if data else "N/A"
            md_exists = "✅" if f.with_suffix(".md").exists() else "❌"
            print(f"  {md_exists} {f.relative_to(root)} → {url}")
        sys.exit(0)

    stats = {"ok": 0, "skip": 0, "error": 0}
    errors = []

    for i, filepath in enumerate(model_files, 1):
        try:
            status, msg = process_model(filepath, root, force=args.force)
        except Exception as e:
            status = "error"
            msg = f"{filepath.relative_to(root)} → 异常: {traceback.format_exc()}"

        stats[status] += 1

        icon = {"ok": "✅", "skip": "⏭️", "error": "❌"}[status]
        print(f"  [{i}/{len(model_files)}] {icon} {msg}")

        if status == "error":
            errors.append(msg)

        # 请求间隔（仅对实际抓取的）
        if status == "ok" and i < len(model_files):
            time.sleep(DELAY)

    print(f"\n{'=' * 60}")
    print(f"  📊 结果: {stats['ok']} 成功, {stats['skip']} 跳过, {stats['error']} 失败")

    if errors:
        print(f"\n  ⚠️  失败列表:")
        for e in errors:
            print(f"    - {e}")

    sys.exit(0 if stats["error"] == 0 else 1)


if __name__ == "__main__":
    main()
