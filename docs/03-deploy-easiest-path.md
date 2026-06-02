# Build and deploy your agent

The easiest "real" deployment for a hackathon team is **a Foundry agent
that your demo points at**. This doc assumes you completed the setup
in `docs/02-foundry-toolkit-tour.md` (extension installed, Azure
prerequisites done, signed in to your Foundry project).

## Before you start: do you have Azure access?

| You have… | What to do | Where to go |
|---|---|---|
| **An endpoint, API key, and agent name from your hackathon coordinator** | They pre-provisioned shared resources. Paste those values into `.env`. Skip the rest of this guide. | Copy `.env.sample` to `.env`, paste the values you were given, then run the samples in `samples/`. |
| **Your own Azure subscription, plus an existing Foundry project** | Reuse the project and add one agent. | **Path A** below. |
| **Your own Azure subscription, but no Foundry project yet** | Provision a fresh environment with `azd up`. | **Path B** below. |
| **No Azure access yet** | Reach out to your hackathon coordinator — most hackathons provision shared resources. | While you wait, you can still ideate with the **kindling** agent and draft a plan with **implementation-plan** in GitHub Copilot Chat. Neither needs Azure. |

If you are unsure which row you are in, ask your coordinator first.
That saves you provisioning something they are already paying for.

## Path A — Use an agent created in the Foundry portal

1. Open your project in the [Microsoft Foundry portal](https://ai.azure.com).
2. Create a new prompt agent. Give it a clear name (for example,
   `kindling-demo-agent`).
3. Pick a chat model deployment (`gpt-4.1-mini` or whatever your org
   has provisioned).
4. Paste a focused system prompt that matches your demo idea. Save the
   agent.
5. Copy the **project endpoint** from the project Overview page.
   It looks like
   `https://<resource>.services.ai.azure.com/api/projects/<project>`.
6. In `.env`, set:
   - `FOUNDRY_PROJECT_ENDPOINT` to the project endpoint from step 5.
   - `FOUNDRY_AGENT_NAME` to the agent name from step 2.
7. Sign in with `az login`, then run `samples/hello-agent-py/app.py`
   to confirm the wiring works. You should see the agent reply in the
   terminal.
8. From there, swap the prompt in `samples/hello-agent-py/app.py` for
   the input your demo actually sends, and let GitHub Copilot help you
   wrap UI or logic around it.

## Path B — Provision a fresh environment with `azd up`

Use this if you don't yet have a Foundry project, or you want a
repeatable environment per team. The kit ships a Bicep template that
creates a Foundry account, a project, a `gpt-4.1-mini` deployment,
Log Analytics, and Application Insights.

1. Install the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd).
2. From the repo root, run `azd auth login`, then `azd up`.
3. When prompted, pick a region close to your team that supports the
   Foundry Agent Service and `gpt-4.1-mini`. EU teams:
   `swedencentral`. US teams: `eastus2`. Full list:
   [Azure OpenAI Responses API supported regions](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/responses#supported-regions).
4. Bootstrap your local `.env` from the deployment outputs.

   > ⚠️ This **replaces** your local `.env`. If you already have one
   > with values you want to keep, the snippets below back it up to
   > `.env.backup` first.

   ```powershell
   if (Test-Path .env) { Copy-Item .env .env.backup -Force }
   azd env get-values | Out-File -FilePath .env -Encoding utf8
   ```

   ```bash
   if [ -f .env ]; then cp .env .env.backup; fi
   azd env get-values > .env
   ```

   This writes `FOUNDRY_PROJECT_ENDPOINT`, `AZURE_OPENAI_ENDPOINT`,
   `AZURE_OPENAI_DEPLOYMENT_NAME`, and a few others directly into
   `.env`.
5. Fetch the Azure OpenAI key separately (Bicep does not output
   secrets):

   ```powershell
   $accountName = azd env get-value AZURE_AIFOUNDRY_NAME
   $rg = azd env get-value AZURE_RESOURCE_GROUP
   az cognitiveservices account keys list --name $accountName --resource-group $rg --query key1 -o tsv
   ```

   ```bash
   ACCOUNT_NAME=$(azd env get-value AZURE_AIFOUNDRY_NAME)
   RG=$(azd env get-value AZURE_RESOURCE_GROUP)
   az cognitiveservices account keys list --name "$ACCOUNT_NAME" --resource-group "$RG" --query key1 -o tsv
   ```

   Append the result to `.env` as `AZURE_OPENAI_API_KEY=<the-key>`.
6. Run `samples/hello-foundry-py/app.py` to confirm the model
   deployment is reachable from code.
7. In the [Foundry portal](https://ai.azure.com), open the project
   and create a prompt agent against the `gpt-4.1-mini` deployment
   (steps 2–4 of Path A). Add `FOUNDRY_AGENT_NAME=<agent-name>` to
   `.env`.
8. Run `samples/hello-agent-py/app.py` to confirm the agent wiring.

## Success criterion

The deployed version should be easy to explain, easy to refresh, and
easy to show to a live audience. If you can hit refresh and re-run the
demo cleanly on stage, you are in good shape.

## When you outgrow this deployment

For richer orchestration, Azure-platform deployment patterns,
governance, and other directions beyond the spark, see
`docs/05-going-further.md`.
