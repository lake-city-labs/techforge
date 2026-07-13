# TechForge.Briefing.v1

Daily AI and technology intelligence briefings powered by Grok.

## Quick Start

### 1. Environment Variables
Create a `.env` file in the project root with:

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

The `launchd` job is already installed and loaded.

To reload after changes:

```bash
launchctl unload ~/Library/LaunchAgents/com.lakecitylabs.techforge.plist
launchctl load ~/Library/LaunchAgents/com.lakecitylabs.techforge.plist
```

Logs are written to:
- `logs/techforge.log`
- `logs/techforge-error.log`

## Output

- Full briefing: `artifacts/tech-digests/YYYY-MM-DD.md`
- Discord summary posted to `cassius-updates`

## Repo

https://github.com/lake-city-labs/techforge