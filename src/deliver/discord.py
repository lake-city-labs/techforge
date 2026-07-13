"""
Real Discord delivery for TechForge briefings
"""
import os
import subprocess
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


def get_discord_bot_token() -> Optional[str]:
    """Try to get the Discord bot token from OpenClaw config first, then env."""
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

    return os.getenv("DISCORD_BOT_TOKEN")


def post_to_discord(
    message: str,
    channel_id: str = "1490929063299383328",
    bot_token: Optional[str] = None
) -> bool:
    """Post a message to Discord."""
    if not bot_token:
        bot_token = get_discord_bot_token()

    if not bot_token:
        print("[Discord] No bot token found")
        print(message[:800] + "..." if len(message) > 800 else message)
        return False

    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json",
    }
    payload = {"content": message}

    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        print(f"[Discord] Posted to channel {channel_id}")
        return True
    except Exception as e:
        print(f"[Discord] Failed to post: {e}")
        return False


def format_discord_summary(briefing: str, date_str: str) -> str:
    """
    Create a skimmable Discord version.
    Discord allows ~2000 characters. We aim for ~1800 max.
    """
    # Try to find a good cutoff point (after Top Signals section)
    cutoff_markers = [
        "## AI/Agents Spotlight",
        "## Contech Corner",
        "## What to Watch",
        "\n\n## "
    ]
    
    max_length = 1800
    summary = briefing[:max_length]
    
    # Try to cut at a logical section
    for marker in cutoff_markers:
        if marker in summary:
            summary = summary.split(marker)[0].strip()
            break
    
    if len(briefing) > len(summary):
        summary += "\n\n... (full version linked below)"

    return f"""**TechForge Briefing — {date_str}**

{summary}

**Live version:** https://YOUR-USERNAME.github.io/techforge/{date_str}.html
**Full report:** https://github.com/lake-city-labs/techforge/tree/main/artifacts/tech-digests/{date_str}.html"""