# Deploy the easiest path

The easiest "real" deployment for a hackathon team is **a Foundry agent that
your demo points at**. There are two paths — pick whichever fits your team.

## Path A — Use an agent created in the Foundry portal (truly the easiest)

1. Open your project in the [Microsoft Foundry portal](https://ai.azure.com).
2. Create a new prompt agent. Give it a clear name (for example, `kindling-demo-agent`).
3. Pick a chat model deployment (`gpt-4.1-mini` or whatever your org has provisioned).
4. Paste a focused system prompt that matches your demo idea. Save the agent.
5. Copy the **project endpoint** from the project Overview page.
   It looks like `https://<resource>.services.ai.azure.com/api/projects/<project>`.
6. In `.env`, set:
   - `FOUNDRY_PROJECT_ENDPOINT` to the project endpoint from step 5.
   - `FOUNDRY_AGENT_NAME` to the agent name from step 2.
7. Sign in with `az login`, then run `samples/hello-agent-py/app.py` to confirm
   the wiring works. You should see the agent reply in the terminal.
8. From there, swap the prompt in `samples/hello-agent-py/app.py` for the input
   your demo actually sends, and let GitHub Copilot help you wrap UI or logic
   around it.

## Path B — Provision a fresh hackathon environment with `azd up`

Use this if you don't yet have a Foundry project, or you want a repeatable
environment per team. The kit ships a Bicep template that creates a Foundry
account, a project, a `gpt-4.1-mini` deployment, Log Analytics, and
Application Insights.

1. Install the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd).
2. From the repo root, run `azd auth login`, then `azd up`.
3. When prompted, pick a region close to your team that supports the Foundry
   Agent Service and `gpt-4.1-mini`. EU teams: `swedencentral`. US teams:
   `eastus2`. Full list: [Azure OpenAI Responses API supported regions](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/responses#supported-regions).
4. `azd up` prints the deployed resource names. Note the **Foundry account
   name** and **project name**.
5. In the Foundry portal, open the project and create an agent against the
   `gpt-4.1-mini` deployment (steps 2–4 of Path A).
6. Continue from step 5 of Path A to wire `.env` and run the sample.

## Success criterion

The deployed version should be easy to explain, easy to refresh, and easy to
show to a live audience. If you can hit refresh and re-run the demo cleanly
on stage, you are in good shape.

## When you outgrow this deployment

For richer orchestration, Azure-platform deployment patterns, governance,
and other directions beyond the spark, see `docs/05-going-further.md`.
