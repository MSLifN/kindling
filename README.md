# Kindling

A small repo that lights your hackathon fire.

Kindling is a reusable starter kit for building AI tools with GitHub Copilot + Foundry Toolkit in one focused, low-friction repo. The Foundry Toolkit is Microsoft's VS Code extension for Azure AI Foundry — browse models, test prompts in a playground, and reference the agents you build in your Foundry project. Kindling keeps a hackathon practical: bring the spark, build fast, and leave with something demoable.

## Why this kit exists

This repo is designed for short-fuse hackathons where you have hours, not weeks:
- Start with a working idea in minutes.
- Use GitHub Copilot and Foundry Toolkit to prototype an agent or model flow quickly.
- Keep the path to a live demo short, simple, and repeatable.

## What is inside

- Custom agents in `.github/agents/` for GitHub Copilot Chat handoffs and quick idea generation, planning, and storytelling.
- Two ready-to-run hello samples — one for an Azure OpenAI model call and one for a Foundry agent — that verify your setup end to end.
- Three starter ideas for small, practical AI tools you'd actually use yourself:
  - **Data Buddy** — turns "what does this column actually mean?" into a one-line answer.
  - **Meeting Summarizer** — turns "I'll write that up later" into action items already in the channel.
  - **Personal Knowledge Bot** — captures and retrieves your own scattered notes in plain language.

## How to use this kit

Two layers, that's it:

1. **Spark path (this kit)** — ideate in GitHub Copilot Chat with the
   **kindling** agent, validate your setup with the samples, build something
   demoable.
2. **Going further** — when the demo becomes a product, see
   `docs/05-going-further.md` for curated external projects (Agent
   Framework, Azure AI landing zone, Citadel governance, and other
   community resources).

## How your team fits

Hackathon teams are rarely all engineers. Use the kit where you sit:

- **Engineers** — follow the Setup section below to install dependencies
  and validate the samples, then build with GitHub Copilot Chat
  (select the **kindling** agent) and the Foundry Toolkit.
- **PMs and customer-facing roles** — read `starter-ideas/` for build
  inspiration, and lift the prompts from the agent files in
  `.github/agents/` into any GitHub Copilot Chat session as reusable
  templates for ideation, planning, and demo storytelling. No
  Kindling install required.
- **Designers and storytellers** — focus on
  `docs/01-vibe-coding-101.md`, `.github/agents/demo-storyteller.agent.md`,
  and the demo angle in each starter idea. Shape the user-facing flow that
  the engineers will wrap code around.

## Setup

1. Open this folder in VS Code.
2. Install the [.NET Runtime](https://learn.microsoft.com/en-us/dotnet/core/install/) if you don't already have it — Foundry Toolkit requires it.
3. Install the recommended extensions from `.vscode/extensions.json` — Foundry Toolkit and Python. (GitHub Copilot is built into VS Code and does not need a separate install.)
   - Terminal option:
     ```powershell
     Get-Content .\.vscode\extensions.json -Raw | ConvertFrom-Json | Select-Object -ExpandProperty recommendations | ForEach-Object { code --install-extension $_ }
     ```
     If `code` is not on PATH, run “Shell Command: Install 'code' command in PATH” once in VS Code first.
4. Decide where your Foundry endpoint comes from
   `.env`. Read the **Before you start** table at the top of
   `docs/03-deploy-easiest-path.md` and pick your row:
   - **Coordinator-provided values** — paste them into `.env` and
     jump straight to step 5 below.
   - **Self-serve with an existing Foundry project** — follow
     **Path A** in `docs/03-deploy-easiest-path.md`.
   - **Self-serve with `azd up`** — follow **Path B** in
     `docs/03-deploy-easiest-path.md`.
   - **No Azure access yet** — reach out to your hackathon
     coordinator. While you wait, you can still ideate with
     the **kindling** agent in GitHub Copilot Chat — no Azure required.
5. Install the Python dependencies:
   - **Windows:** `py -3.12 -m pip install -r requirements.txt`
   - **macOS / Linux:** `python3 -m pip install -r requirements.txt`
6. Run the samples (use `py -3.12` on Windows or `python3` on macOS / Linux):
   - `samples/hello-foundry-py/app.py`
   - `samples/hello-agent-py/app.py`

## Recommended flow

1. Pick a starter idea from `starter-ideas/`.
2. Switch to the **kindling** agent using the agent selector in GitHub Copilot Chat, then follow the handoff buttons through ideation → planning → demo story.
3. Validate your environment by running the samples in `samples/` — they prove that the code GitHub Copilot suggests can actually reach Foundry end to end.
4. Move to `docs/05-going-further.md` for curated external references and `docs/06-planning-team-setup.md` for organizer setup when the spark becomes a shared effort.

Tips:

- **Selecting an agent** — open any GitHub Copilot Chat panel in
  VS Code and use the **agent selector** (the dropdown at the top of
  the chat) to pick `kindling` or any of the other custom agents.
  The custom agents in `.github/agents/` are loaded by GitHub Copilot
  in VS Code only — they don't appear in browser GitHub Copilot Chat.
- **Agents not showing up?** — GitHub Copilot is built into VS Code,
  but its Chat panel must be visible for the agent selector to appear.
  Open the Command Palette and run "Chat: Open Customizations" to
  confirm the four agents are detected. If they still don't appear,
  make sure this workspace folder is the one open in VS Code (the
  agents live in `.github/agents/` relative to the workspace root).
- **Browsing the agents** — open the Command Palette and run
  "Chat: Open Customizations" to see all four custom agents this kit
  ships.

## More docs

- `docs/01-vibe-coding-101.md` — fast prototyping with GitHub Copilot
- `docs/02-foundry-toolkit-tour.md` — install, Azure prerequisites, sidebar tour, and Copilot tools
- `docs/03-deploy-easiest-path.md` — build and deploy your Foundry agent (Path A or Path B)
- `docs/04-event-criteria.md` — slot for your hackathon's judging criteria
- `docs/05-going-further.md` — community projects and deeper GitHub Copilot references
- `docs/06-planning-team-setup.md` — per-team Foundry projects, RBAC, and shared resources for organizers

