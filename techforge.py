#!/usr/bin/env python3
"""
TechForge.Briefing.v1
Daily AI/technology intelligence briefing generator.
"""
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent / "src"))

from config import load_sources
from ingest import fetch_rss, fetch_hn_top
from normalize import deduplicate
from synthesize import generate_briefing
from deliver import save_briefing, post_to_discord, format_discord_summary


def run_daily_briefing():
    """Full daily briefing pipeline."""
    print("=== TechForge.Briefing.v1 ===\n")

    # 1. Ingestion
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
    unique_items = deduplicate(all_items)
    print(f"Total items after dedup:  {len(unique_items)}")

    # 2. Synthesis
    print("\nGenerating briefing with Grok...")
    briefing = generate_briefing(unique_items)

    # 3. Delivery
    date_str = datetime.now().strftime("%Y-%m-%d")
    save_briefing(briefing, date_str)

    discord_msg = format_discord_summary(briefing, date_str)
    post_to_discord(discord_msg)

    print("\n=== Briefing complete ===")
    return briefing


if __name__ == "__main__":
    run_daily_briefing()