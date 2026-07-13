"""
Hacker News Ingestion via Firebase API
"""
import requests
from datetime import datetime, timezone
from typing import List, Dict, Any


HN_TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{id}.json"


def fetch_hn_top(limit: int = 30) -> List[Dict[str, Any]]:
    """Fetch top stories from Hacker News."""
    try:
        resp = requests.get(HN_TOP_STORIES, timeout=15)
        resp.raise_for_status()
        ids = resp.json()[:limit]

        items = []
        for item_id in ids:
            item_resp = requests.get(HN_ITEM.format(id=item_id), timeout=10)
            if item_resp.status_code != 200:
                continue
            data = item_resp.json()
            if not data or data.get("dead") or data.get("deleted"):
                continue

            items.append({
                "source": "Hacker News",
                "type": "hn",
                "title": data.get("title", ""),
                "url": data.get("url", f"https://news.ycombinator.com/item?id={item_id}"),
                "score": data.get("score", 0),
                "hn_id": item_id,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            })

        return items
    except Exception as e:\n        print(f"HN fetch error: {e}")
        return []