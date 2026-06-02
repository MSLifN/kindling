# Foundry Toolkit in VS Code

The Foundry Toolkit is Microsoft's VS Code extension for Azure AI
Foundry — browse models, deploy them, try prompts in a playground, and
reference the agents you build in the Foundry portal. In Kindling it
is the "build half": GitHub Copilot writes the code, Foundry Toolkit
gives you the models and agent surface to call from it.

Official docs:

- [Foundry Toolkit overview (code.visualstudio.com)](https://code.visualstudio.com/docs/intelligentapps/overview)
  — install, sign-in, and the full feature tour.
- [Azure AI Foundry Agent Service overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)
  — what an agent actually is on the platform side.

## Kindling-specific bullets

- The extension ID Kindling installs is
  `ms-windows-ai-studio.windows-ai-studio` (see `.vscode/extensions.json`).
- For this kit, deploy `gpt-4.1-mini` (Global Standard, capacity 1) into
  your Foundry project — it is cheap, fast, and matches the Bicep
  default in `infra/main.bicep`.
- Use the **Playground** view to iterate on a system prompt before
  pasting it into the agent in the Foundry portal.
- Use the **Models** view to copy the deployment name and endpoint
  into `.env`. Those two values are what `samples/hello-foundry-py/app.py`
  reads.
- Agent authoring itself lives in the Foundry portal at
  https://ai.azure.com. Jump there when the toolkit doesn't yet expose
  the feature you need.

When the wiring works, return to `docs/03-deploy-easiest-path.md` for
the minimal end-to-end deploy.
