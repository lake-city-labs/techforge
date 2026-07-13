"""
Configuration loader
"""
import yaml
from pathlib import Path
from typing import Dict, Any


def load_sources(config_path: str = "config/sources.yaml") -> Dict[str, Any]:
    """Load source configuration."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    with open(path, "r") as f:\n        return yaml.safe_load(f)