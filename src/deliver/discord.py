"""
Discord delivery for TechForge briefings
"""
from typing import Optional


def post_to_discord(message: str, channel_id: str = "1490929063299383328") -> bool:
    """
    Post a message to the cassius-updates Discord channel.
    This is a stub — will be wired to the actual Discord client.
    """
    print(f"[Discord] Would post to channel {channel_id}")
    print(f"[Discord] Message length: {len(message)} chars")
    # In production: use discord.py or OpenClaw Discord skill
    return True


def format_discord_summary(briefing: str) -> str:
    """Create a skimmable Discord version of the briefing."""
    # For v1, just return a truncated version with link
    return f"""**TechForge Briefing** (full version in repo)

{briefing[:800]}...

Full report: https://github.com/lake-city-labs/techforge/tree/main/artifacts/tech-digests
"""
