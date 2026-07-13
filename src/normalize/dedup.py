"""
Basic deduplication utilities
"""
from typing import List, Dict, Any
from difflib import SequenceMatcher


def normalize_url(url: str) -> str:
    """Basic URL normalization."""
    if not url:
        return ""
    return url.split("#")[0].rstrip("/")


def similar(a: str, b: str) -> float:
    """Simple string similarity."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def deduplicate(items: List[Dict[str, Any]], threshold: float = 0.85) -> List[Dict[str, Any]]:
    """Remove near-duplicate items based on title similarity and URL."""
    seen = []
    unique = []

    for item in items:
        url = normalize_url(item.get("url", ""))
        title = item.get("title", "")

        is_duplicate = False
        for existing in seen:
            if url and url == existing.get("url"):
                is_duplicate = True
                break
            if similar(title, existing.get("title", "")) > threshold:
                is_duplicate = True
                break

        if not is_duplicate:
            seen.append({"url": url, "title": title})
            unique.append(item)

    return unique
