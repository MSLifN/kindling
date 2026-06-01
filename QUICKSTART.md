# QUICKSTART: 30-minute live demo path

This is the fastest path to a visible demo for a Microsoft hackathon slot.

## 0. Before you start (2 minutes)

- Open the repo in VS Code and follow the setup steps in `README.md`.
- Install the recommended extensions from `.vscode/extensions.json`.
- Copy `.env.sample` to `.env`.
- Install the Python dependencies with `py -3.12 -m pip install -r requirements.txt`.

## 1. Choose a starter idea (3 minutes)

Pick one of these:
- `starter-ideas/meeting-summarizer.md`
- `starter-ideas/data-buddy.md`
- `starter-ideas/personal-knowledge-bot.md`

## 2. Ask the agent to define the first pulse (5 minutes)

Use the agent prompts in `agents/` to:
- sharpen the use case
- describe the user value
- identify the one demo action the user can see immediately

## 3. Run the hello samples (5 minutes)

- `py -3.12 samples/hello-foundry-py/app.py` to confirm model access
- `py -3.12 samples/hello-agent-py/app.py` to confirm agent-service flow

## 4. Vibe-code the core flow (10 minutes)

Use Copilot + Foundry Toolkit to build:
1. one simple input
2. one simple AI response
3. one clear output for the audience

## 5. Optional cloud path (5 minutes)

Follow `docs/03-deploy-easiest-path.md` to launch the simplest Foundry Agent Service deployment.

## 6. Troubleshooting

If the sample does not run, start with `TROUBLESHOOTING.md`.

## 7. Demo script (30-second pitch)

"This is an AI tool for ourselves. It helps us move from idea to prototype in minutes, using Copilot and Foundry to build something practical and showable."
