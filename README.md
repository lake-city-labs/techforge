# TechForge.Briefing.v1

Daily AI and technology intelligence briefings powered by Grok.

## GitHub Pages (Live Website)

HTML versions are automatically generated in the `docs/` folder.

### Enable GitHub Pages

1. Go to your repo → **Settings** → **Pages**
2. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: `main`
   - Folder: `/docs`
3. Save

Your briefings will be live at:
`https://YOUR-USERNAME.github.io/techforge/YYYY-MM-DD.html`

## Quick Start

### Environment Variables
Create a `.env` file:

```env
XAI_API_KEY=***
DISCORD_BOT_TOKEN=***
```

### Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### Test Run

```bash
python3 techforge.py
```

### Daily Automation

Already set up via `launchd` (runs at 7:00 AM daily).

Logs: `logs/techforge.log`

## Output Locations

- Markdown: `artifacts/tech-digests/YYYY-MM-DD.md`
- HTML: `artifacts/tech-digests/YYYY-MM-DD.html` + `docs/YYYY-MM-DD.html`
- Discord: Posted to `cassius-updates`

## Repo

https://github.com/lake-city-labs/techforge