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

## Four layers of the kit

1. Spark path — the fast, low-friction demo flow for teams trying the repo for the first time.
2. Next-level path — a developer-focused layer for teams who want to experiment with Microsoft Agent Framework and richer local orchestration.
3. Azure platform path — an extra layer for teams who want to extend the prototype into an Azure AI landing zone and deploy with azd.
4. Governance path — for teams who want to harden the prototype with Citadel-style governance, observability, and compliance patterns before scaling.

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
4. Move to the advanced docs in `docs/` if you want to deepen the implementation.

Tip: open the Command Palette and run “Chat: Open Customizations” to browse the custom agents this kit ships.

## Next-level paths

- For developer experiments: see `docs/05-agent-framework-next-level.md`.
- For Azure deployment and landing-zone thinking: see `docs/06-azure-ai-landing-zone-azd.md`.
- For governance, observability, and production-hardening ideas: see `docs/07-citadel-governance-path.md`.
- For hackathon planning and team access setup: see `docs/08-planning-team-setup.md`.

