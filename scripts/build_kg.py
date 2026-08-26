#!/usr/bin/env python3
"""Build a LightRAG knowledge graph from all markdown files in the repository.

This script reads all .md files from domains/, platforms/, and docs/ directories,
then inserts them into a LightRAG instance to build a knowledge graph.

Usage:
    python scripts/build_kg.py

Environment variables:
    ZHIPUAI_API_KEY  - Zhipu AI API key (defaults to project key if not set)
    KG_MODEL         - LLM model name (default: glm-4-flash)
    KG_WORKING_DIR   - Knowledge graph storage directory (default: ./kg_data)
"""

import asyncio
import os
import sys
from pathlib import Path

# Ensure the project root is discoverable
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def collect_markdown_files() -> list[Path]:
    """Collect all .md files from domains/, platforms/, and docs/ directories."""
    md_files = []
    search_dirs = [
        PROJECT_ROOT / "domains",
        PROJECT_ROOT / "platforms",
        PROJECT_ROOT / "docs",
    ]
    for search_dir in search_dirs:
        if search_dir.exists():
            md_files.extend(sorted(search_dir.rglob("*.md")))
    return md_files


async def build_knowledge_graph():
    """Build the knowledge graph from markdown files."""
    from lightrag import LightRAG
    from lightrag.llm.zhipu import zhipu_complete, zhipu_embedding

    # Configuration
    api_key = os.environ.get(
        "ZHIPUAI_API_KEY", "ac96a781bad141808246da37f274d99a.1w0Oib3gCblk4rC3"
    )
    model = os.environ.get("KG_MODEL", "glm-4-flash")
    working_dir = os.environ.get("KG_WORKING_DIR", str(PROJECT_ROOT / "kg_data"))

    # Ensure working directory exists
    os.makedirs(working_dir, exist_ok=True)

    print(f"Knowledge graph working directory: {working_dir}")
    print(f"Using model: {model}")

    # Initialize LightRAG with Zhipu backend
    rag = LightRAG(
        working_dir=working_dir,
        llm_model_func=zhipu_complete,
        llm_model_kwargs={
            "model": model,
            "api_key": api_key,
        },
        embedding_func=zhipu_embedding,
        embedding_batch_num=8,
        llm_model_max_async=4,
    )

    # Collect markdown files
    md_files = collect_markdown_files()
    print(f"Found {len(md_files)} markdown files to process")

    if not md_files:
        print("No markdown files found. Exiting.")
        return

    # Read and insert documents
    documents = []
    for md_file in md_files:
        relative_path = md_file.relative_to(PROJECT_ROOT)
        content = md_file.read_text(encoding="utf-8")
        # Prepend file path as metadata context
        doc_content = f"[Source: {relative_path}]\n\n{content}"
        documents.append(doc_content)
        print(f"  Loaded: {relative_path} ({len(content)} chars)")

    print(f"\nInserting {len(documents)} documents into knowledge graph...")
    print("This may take several minutes depending on API rate limits.\n")

    # Insert documents in batches to avoid overwhelming the API
    batch_size = 5
    for i in range(0, len(documents), batch_size):
        batch = documents[i : i + batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(documents) + batch_size - 1) // batch_size
        print(f"Processing batch {batch_num}/{total_batches}...")
        try:
            await rag.ainsert(batch)
        except Exception as e:
            print(f"  Warning: Error processing batch {batch_num}: {e}")
            print("  Continuing with next batch...")
            continue

    print("\nKnowledge graph build complete!")
    print(f"Data stored in: {working_dir}")


def main():
    """Entry point."""
    print("=" * 60)
    print("LightRAG Knowledge Graph Builder")
    print("=" * 60)
    print()

    asyncio.run(build_knowledge_graph())


if __name__ == "__main__":
    main()
