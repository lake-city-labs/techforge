"""
File delivery for TechForge briefings
"""
from datetime import datetime
from pathlib import Path


def save_briefing(briefing: str, date_str: Optional[str] = None) -> Path:
    """Save the full briefing to artifacts/tech-digests/."""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    output_dir = Path("artifacts/tech-digests")
    output_dir.mkdir(parents=True, exist_ok=True)

    filepath = output_dir / f"{date_str}.md"
    filepath.write_text(briefing)

    print(f"[File] Saved briefing to {filepath}")
    return filepath
