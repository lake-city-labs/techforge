# TechForge.Briefing.v1

Daily AI and technology intelligence briefings powered by Grok.

## Purpose
TechForge produces a high-signal daily briefing focused on AI, agents, tooling, research, and infrastructure. It is designed to be read like a sharp analyst summary rather than a news digest.

## Structure
- `config/sources.yaml` — Curated ingestion sources
- `prompts/briefing.md` — Analyst system prompt
- `artifacts/tech-digests/` — Daily Markdown briefings (committed to repo)
- `src/` — Ingestion, normalization, synthesis, and delivery logic

## Current Status
v1 in development. Focused on RSS + HN ingestion with Grok-powered synthesis.

## Output
- Full briefing: `artifacts/tech-digests/YYYY-MM-DD.md`
- Discord summary posted to `cassius-updates`

## Repo
https://github.com/lake-city-labs/techforge