"""
RSS Feed Ingestion
"""
import feedparser
from datetime import datetime, timezone
from typing import List, Dict, Any


def fetch_rss(url: str, source_name: str) -> List[Dict[str, Any]]:
    """Fetch and parse an RSS feed."""
    feed = feedparser.parse(url)
    items = []

    for entry in feed.entries:
        item = {
            "source": source_name,
            "type": "rss",
            "title": entry.get("title", ""),
            "url": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", ""),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }
        items.append(item)

    return items