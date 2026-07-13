"""
Briefing synthesis using Grok (xAI)
"""
import os
from typing import List, Dict, Any
from openai import OpenAI

from .prompts import ANALYST_SYSTEM_PROMPT


def build_briefing_context(items: List[Dict[str, Any]], max_items: int = 25) -> str:
    """Build a compact context string from items for the LLM."""
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
    Generate the daily briefing using Grok via xAI API.
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

    # Initialize xAI client (OpenAI compatible)
    client = OpenAI(
        api_key=os.getenv("XAI_API_KEY", "your-api-key-here"),
        base_url="https://api.x.ai/v1"
    )

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": ANALYST_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=4000,
        )

        return response.choices[0].message.content

    except Exception as e:\n        return f"""[ERROR] Failed to generate briefing with Grok: {e}

Fallback placeholder briefing would go here.
"""
