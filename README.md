# Kindling

A small repo that lights your hackathon fire.

Kindling is a reusable starter kit for building AI tools with Copilot + Foundry Toolkit in one focused, low-friction repo. It keeps the "AI Ourselves" theme practical: bring the spark, build fast, and leave with something demoable.

## Why this kit exists

This repo is designed for the "AI Ourselves" theme:
- Start with a working idea in minutes.
- Use Copilot and Foundry Toolkit to prototype an agent or model flow quickly.
- Keep the path to a live demo short, simple, and repeatable.

## What is inside

- Custom agents in `.github/agents/` for Copilot Chat handoffs and quick idea generation, planning, and storytelling.
- Ready-to-run sample code for a Foundry model call and an agent-service call.
- A 30-minute live-demo path with copy-ready steps.
- Starter ideas that help teams choose a direction fast.

## How to use this kit

Two layers, that's it:

1. **Spark path (this kit)** — ideate fast in Copilot Chat, validate with
   the samples, demo in 30 minutes.
2. **Going further** — when the demo becomes a product, see
   `docs/05-going-further.md` for curated external projects (Agent
   Framework, Azure AI landing zone, Citadel governance, awesome-copilot).

## 5-minute setup

1. Open this folder in VS Code.
2. Install the recommended extensions from .vscode/extensions.json.
   - Terminal option:
     ```powershell
     Get-Content .\.vscode\extensions.json -Raw | ConvertFrom-Json | Select-Object -ExpandProperty recommendations | ForEach-Object { code --install-extension $_ }
     ```
     If `code` is not on PATH, run “Shell Command: Install 'code' command in PATH” once in VS Code first.
3. Copy `.env.sample` to `.env` and fill in the required values.
4. Install the Python dependencies with `py -3.12 -m pip install -r requirements.txt`.
5. Run the samples:
   - `py -3.12 samples/hello-foundry-py/app.py`
   - `py -3.12 samples/hello-agent-py/app.py`
6. Start with `QUICKSTART.md` for the stage-ready demo path.

## Recommended flow

1. Pick a starter idea from `starter-ideas/`.
2. Switch to the `@kindling` custom agent in Copilot Chat, then follow the handoff buttons through ideation → planning → demo story.
3. Validate with `samples/`.
4. Move to `docs/05-going-further.md` for curated external references and `docs/06-planning-team-setup.md` for organizer setup when the spark becomes a shared effort.

Tip: open the Command Palette and run “Chat: Open Customizations” to browse the custom agents this kit ships.

## More docs

- `docs/01-vibe-coding-101.md` — fast prototyping principles
- `docs/02-foundry-toolkit-tour.md` — orient in VS Code
- `docs/03-deploy-easiest-path.md` — minimal Foundry Agent Service deploy
- `docs/04-event-criteria.md` — slot for your hackathon's judging criteria
- `docs/05-going-further.md` — where to go when the spark catches
- `docs/06-planning-team-setup.md` — RBAC and shared resources for organizers

