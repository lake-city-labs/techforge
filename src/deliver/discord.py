"""
Real Discord delivery for TechForge briefings
"""
import os
import subprocess
import requests
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_discord_bot_token() -> Optional[str]:
    """
    Try to get the Discord bot token from OpenClaw config first,
    then fall back to environment variable.
    """
    # Try OpenClaw config
    try:
        result = subprocess.run(
            ["openclaw", "config", "get", "discord.bot_token"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass

    # Fall back to environment variable
    return os.getenv("DISCORD_BOT_TOKEN")


def post_to_discord(
    message: str,
    channel_id: str = "1490929063299383328",
    bot_token: Optional[str] = None
) -> bool:
    """
    Post a message to Discord using the bot token.
    """
    if not bot_token:
        bot_token = get_discord_bot_token()

    if not bot_token:
        print("[Discord] No bot token found (checked OpenClaw config + DISCORD_BOT_TOKEN env var)")
        print("[Discord] Message would be:")
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
    except Exception as e:
        print(f"[Discord] Failed to post: {e}")
        return False


def format_discord_summary(briefing: str, date_str: str) -> str:
    """Create a skimmable Discord version of the briefing."""
    summary = briefing[:1500]
    if len(briefing) > 1500:
        summary += "..."

    return f"""**TechForge Briefing — {date_str}**

{summary}

Full report: https://github.com/lake-city-labs/techforge/tree/main/artifacts/tech-digests/{date_str}.md
"""