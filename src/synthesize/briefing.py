"""
Briefing synthesis using Grok (xAI) via direct HTTP
"""
import os
from dotenv import load_dotenv
import requests
from typing import List, Dict, Any

from .prompts import ANALYST_SYSTEM_PROMPT

# Load environment variables from .env file
load_dotenv()


def build_briefing_context(items: List[Dict[str, Any]], max_items: int = 60) -> str:
    """
    Build a compact context string from items for the LLM.
    
    TODO: Make this smarter over time:
    - Prioritize by source weight (from config)
    - Boost items with scores (HN)
    - Recency weighting
    - Deduplicate more aggressively at context level
    """
    context_lines = []
    for i, item in enumerate(items[:max_items], 1):
        title = item.get("title", "")
        source = item.get("source", "")
        url = item.get("url", "")
        score = item.get("score", "")

        line = f"{i}. [{source}] {title}"
        if score:
            line += f" (HN: {score})"
        if url:
            line += f" — {url}"
        context_lines.append(line)

    return "\n".join(context_lines)


def generate_briefing(items: List[Dict[str, Any]], model: str = "grok-4.3") -> str:
    """
    Generate the daily briefing using Grok via direct xAI API call.
    """
    context = build_briefing_context(items)

    user_prompt = f"""Here are today's top technology stories after deduplication:

{context}

Please produce a high-quality daily briefing in this exact structure:

# TechForge Briefing — [Today's Date]

## Macro Read (2-3 sentences)

## Top Signals
- **Signal 1 Title**
  - What happened
  - Why it matters now
  - Implications for AI/agent builders
  (Sources: ...)

(repeat for 6-10 signals)

## AI/Agents Spotlight
(deeper section on the most important AI/agent developments)

## Contech Corner
(only if genuinely relevant — keep very short)

## What to Watch
(open questions or emerging threads)

Write with the analyst voice defined in the system prompt.
"""

    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        return "[ERROR] XAI_API_KEY environment variable not set."

    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": ANALYST_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 4000,
    }

    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"""[ERROR] Failed to generate briefing with Grok: {e}

Fallback placeholder briefing would go here.
"""