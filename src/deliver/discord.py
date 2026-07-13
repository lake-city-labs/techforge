"""
Real Discord delivery for TechForge briefings
"""
import os
import requests
from typing import Optional


def post_to_discord(
    message: str,
    channel_id: str = "1490929063299383328",
    bot_token: Optional[str] = None
) -> bool:
    """
    Post a message to Discord using the bot token.
    Falls back to printing if no token is provided.
    """
    if not bot_token:
        bot_token = ***"DISCORD_BOT_TOKEN")

    if not bot_token:
        print("[Discord] No bot token found. Message would be:")
        print(message[:500] + "..." if len(message) > 500 else message)
        return False

    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "content": message
    }

    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        print(f"[Discord] Posted to channel {channel_id}")
        return True
    except Exception as e:\n        print(f"[Discord] Failed to post: {e}")
        return False


def format_discord_summary(briefing: str, date_str: str) -> str:
    """Create a skimmable Discord version of the briefing."""
    # Take first ~1500 chars and add link to full report
    summary = briefing[:1500]
    if len(briefing) > 1500:
        summary += "..."

    return f"""**TechForge Briefing — {date_str}**

{summary}

Full report: https://github.com/lake-city-labs/techforge/tree/main/artifacts/tech-digests/{date_str}.md
"""