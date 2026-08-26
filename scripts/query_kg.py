#!/usr/bin/env python3
"""Query the LightRAG knowledge graph.

This script loads the existing LightRAG instance and queries it with
user-provided text.

Usage:
    python scripts/query_kg.py "What companies work in drug discovery?"
    python scripts/query_kg.py --mode global "Which domains have the most AI models?"
    python scripts/query_kg.py --mode local "Tell me about BloombergGPT"

Modes:
    naive   - Simple text matching without graph traversal
    local   - Search in local subgraph neighborhood
    global  - Search across the entire knowledge graph
    hybrid  - Combine local and global search results
    mix     - Mix of naive and knowledge graph search

Environment variables:
    ZHIPUAI_API_KEY  - Zhipu AI API key (defaults to project key if not set)
    KG_MODEL         - LLM model name (default: glm-4-flash)
    KG_WORKING_DIR   - Knowledge graph storage directory (default: ./kg_data)
"""

import argparse
import asyncio
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

VALID_MODES = ["naive", "local", "global", "hybrid", "mix"]


async def query_knowledge_graph(query: str, mode: str):
    """Query the knowledge graph and print results."""
    from lightrag import LightRAG, QueryParam
    from lightrag.llm.zhipu import zhipu_complete, zhipu_embedding

    # Configuration
    api_key = os.environ.get(
        "ZHIPUAI_API_KEY", "ac96a781bad141808246da37f274d99a.1w0Oib3gCblk4rC3"
    )
    model = os.environ.get("KG_MODEL", "glm-4-flash")
    working_dir = os.environ.get("KG_WORKING_DIR", str(PROJECT_ROOT / "kg_data"))

    if not os.path.exists(working_dir):
        print(f"Error: Knowledge graph data not found at '{working_dir}'.")
        print("Please run 'python scripts/build_kg.py' first to build the graph.")
        sys.exit(1)

    # Initialize LightRAG with same config as build
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

    print(f"Query: {query}")
    print(f"Mode: {mode}")
    print("-" * 60)

    # Execute query
    result = await rag.aquery(query, param=QueryParam(mode=mode))

    print(result)


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Query the LightRAG knowledge graph",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python scripts/query_kg.py "What AI companies work in healthcare?"
    python scripts/query_kg.py --mode global "Which domains have the most AI models?"
    python scripts/query_kg.py --mode local "Tell me about BloombergGPT"
    python scripts/query_kg.py --mode mix "Compare finance and healthcare AI"
        """,
    )
    parser.add_argument("query", help="The query string to search the knowledge graph")
    parser.add_argument(
        "--mode",
        choices=VALID_MODES,
        default="hybrid",
        help="Search mode (default: hybrid)",
    )

    args = parser.parse_args()
    asyncio.run(query_knowledge_graph(args.query, args.mode))


if __name__ == "__main__":
    main()
