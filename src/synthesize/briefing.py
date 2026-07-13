"""
Briefing synthesis using Grok
"""
from typing import List, Dict, Any


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


def generate_briefing(items: List[Dict[str, Any]], model: str = "xai/grok-4.3") -> str:
    """
    Generate the daily briefing using Grok.
    This is a stub ready for model integration.
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

    # Placeholder — in production this will call the Grok model
    return f"""[SYNTHESIS PLACEHOLDER]

System Prompt: {ANALYST_SYSTEM_PROMPT[:100]}...

User Prompt length: {len(user_prompt)} chars

Ready to call model: {model}
"""
