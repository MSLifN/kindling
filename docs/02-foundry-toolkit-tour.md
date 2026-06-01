# Foundry Toolkit tour

The Foundry Toolkit extension for VS Code is the **build half** of this
kit — GitHub Copilot helps you write the code; Foundry Toolkit gives you
the models, playground, and agent surface to call from it.

## Install once

1. Open this folder in VS Code.
2. Accept the prompt to install the recommended extensions, or run them
   from the `.vscode/extensions.json` list. The Foundry Toolkit is
   published under the `ms-windows-ai-studio.windows-ai-studio` ID.
3. Sign in to Azure from the Foundry Toolkit activity-bar view when
   prompted — it reuses your `az login` session.

## What to explore first

Open the Foundry Toolkit icon in the VS Code activity bar. The most
useful views for a hackathon spark are:

- **Catalog** — browse models available in your subscription. Pick
  `gpt-4.1-mini` for a cheap, fast default; switch to a larger model
  only when you have a real reason.
- **Playground** — try prompts against a deployed model without writing
  any code. Iterate on system prompts here before pasting them into the
  agent in the Foundry portal.
- **Models** — see what's deployed in your Foundry account, including
  endpoint URL and deployment name. These are the values you copy into
  `.env`.
- **Agents** — preview prompt agents you've created in the project.
  Agent creation itself happens in the [Foundry portal](https://ai.azure.com).

## Suggested first pass

1. Open the **Catalog**, find `gpt-4.1-mini`, and deploy it (Global Standard,
   capacity 1) into a Foundry project — or use one your organizer has
   already provisioned.
2. Open the **Playground**, point it at that deployment, and verify a
   simple prompt returns a useful reply.
3. Copy the deployment name and Azure OpenAI endpoint into `.env`, then
   run `samples/hello-foundry-py/app.py` to prove the same wiring works
   from code.
4. When you're ready for an agent flow, jump to the
   [Foundry portal](https://ai.azure.com), create a prompt agent against
   that same deployment, and follow `docs/03-deploy-easiest-path.md`.

## How this relates to the portal

The Foundry Toolkit in VS Code is a window into your Foundry project.
The full surface — agent authoring, evaluation runs, content safety
controls, project settings — lives at https://ai.azure.com. Use the
toolkit when you want to stay in your editor; jump to the portal when
you need a feature that's not yet exposed in VS Code.
