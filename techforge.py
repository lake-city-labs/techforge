#!/usr/bin/env python3
"""
TechForge.Briefing.v1
Daily AI/technology intelligence briefing generator.
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from config import load_sources
from ingest import fetch_rss, fetch_hn_top
from normalize import deduplicate


def run_ingestion():
    """Run the full ingestion pipeline."""
    print("Loading sources...")
    config = load_sources()
    sources = config.get("sources", [])

    all_items = []

    for source in sources:
        name = source["name"]
        stype = source["type"]
        url = source.get("url")

        print(f"  Fetching: {name}...")

        if stype == "rss":
            items = fetch_rss(url, name)
            all_items.extend(items)
        elif stype == "hn_firebase":
            items = fetch_hn_top(limit=25)
            all_items.extend(items)

    print(f"\nTotal items before dedup: {len(all_items)}")

    # Deduplicate
    unique_items = deduplicate(all_items)
    print(f"Total items after dedup:  {len(unique_items)}")

    return unique_items


def main():
    print("=== TechForge.Briefing.v1 ===\n")
    items = run_ingestion()
    print(f"\nIngestion complete. {len(items)} unique items ready for synthesis.")


if __name__ == "__main__":
    main()