# Going further

Kindling is a spark, not a platform. When the goal shifts from
"demo this idea" to "ship this idea," explore the projects below.
Each is owned by another team with its own docs — links are starting
points, not promises that the projects stay frozen.

## Build with more structure

- **Microsoft Agent Framework** — code-first agent orchestration when
  you outgrow prompt-and-tool flows. Good fit when you want a reusable
  app pattern instead of a prompt-only prototype.
  https://github.com/microsoft/agent-framework
  https://learn.microsoft.com/agent-framework/

## Deploy with repeatable infrastructure

- **Azure AI Foundry landing zone + azd** — repeatable deployment,
  environment separation, identity, and connectivity guardrails.
  Use when the goal shifts from local demo to shared environment.
  https://github.com/Azure/AI-Landing-Zones

## Govern at scale

- **Citadel reference architecture** — observability, policy enforcement,
  cost controls, and accountable agent identity for production AI.
  Use when "demo this" becomes "run this safely at scale."
  https://github.com/Azure-Samples/foundry-citadel-platform

- **Agent Governance Toolkit** — in-process runtime policy enforcement
  for sensitive agent actions. Pairs with the Citadel patterns above.
  https://github.com/microsoft/agent-governance-toolkit
  https://microsoft.github.io/agent-governance-toolkit

## Extend GitHub Copilot itself

- **awesome-copilot** — community-curated custom agents, instructions,
  skills, hooks, and plugins for GitHub Copilot. Install via the
  marketplace registered in GitHub Copilot CLI / VS Code:
  `copilot plugin install <name>@awesome-copilot`
  https://github.com/github/awesome-copilot
  https://awesome-copilot.github.com
