# TechForge.Briefing.v1

Daily AI and technology intelligence briefings powered by Grok.

## GitHub Pages (Live Website)

HTML versions are generated in `docs/` and the root `index.html` is automatically updated to the latest briefing via GitHub Actions.

The workflow (` .github/workflows/pages.yml `) dynamically copies the most recent digest to `index.html` on every push to `main`.

## Quick Start

### 1. Environment Variables

Create a `.env` file:

```env
XAI_API_KEY=***
DISCORD_BOT_TOKEN=***
```

### 2. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Test Run

```bash
python3 techforge.py
```

### 4. Daily Automation (7 AM)

A `launchd` plist is included in `scripts/com.lakecitylabs.techforge.plist`.

**To use it:**

1. Edit the plist and update the paths to match your machine
2. Copy it to `~/Library/LaunchAgents/`
3. Load it:

```bash
launchctl load ~/Library/LaunchAgents/com.lakecitylabs.techforge.plist
```

Logs are written to `logs/techforge.log` and `logs/techforge-error.log`.

## Output

- Markdown: `artifacts/tech-digests/YYYY-MM-DD.md`
- HTML: `artifacts/tech-digests/YYYY-MM-DD.html` + `docs/YYYY-MM-DD.html`
- Discord: Posted to `cassius-updates`

## Repo

https://github.com/lake-city-labs/techforge