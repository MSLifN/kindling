# Deploy the easiest path

The easiest "real" deployment for a hackathon team is **a Foundry agent that
your demo points at**. There are two paths — pick whichever fits your team.

## Before you start: do you have Azure access?

Before picking a deploy path, figure out which row you're in.

| You have… | What to do | Where to go |
|---|---|---|
| **An endpoint, API key, and agent name from your hackathon coordinator** | They pre-provisioned shared resources. Paste those values into `.env`. Skip the rest of this guide. | Copy `.env.sample` to `.env`, paste the values you were given, then run the samples in `samples/`. |
| **Your own Azure subscription, plus an existing Foundry project** | Reuse the project and add one agent. | **Path A** below. |
| **Your own Azure subscription, but no Foundry project yet** | Provision a fresh environment with `azd up`. | **Path B** below. |
| **No Azure access yet** | Reach out to your hackathon coordinator — most run hackathons provision shared resources. | While you wait, you can still ideate with the **kindling** agent and draft a plan with **implementation-plan** in GitHub Copilot Chat. Neither needs Azure. |

If you are unsure which row you are in, ask your coordinator first.
That saves you provisioning something they are already paying for.

## Prerequisites — resource providers and RBAC

Before you create a Foundry project or publish agents, make sure the
required Azure resource providers are registered in your subscription
and your identity has the right role.

### 1. Register resource providers (once per subscription)

```powershell
az provider register --namespace Microsoft.CognitiveServices --wait
az provider register --namespace Microsoft.MachineLearningServices --wait
```

Verify with:

```powershell
az provider show --namespace Microsoft.CognitiveServices --query registrationState -o tsv
az provider show --namespace Microsoft.MachineLearningServices --query registrationState -o tsv
```

Both should return `Registered`. If they don't, you may need
subscription-level Contributor or Owner to register them — ask your
coordinator.

### 2. Grant the right Foundry roles

The [official RBAC reference](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry)
defines two scopes and two key roles.

| Who | Role | Scope | Lets you… |
|---|---|---|---|
| Every participant | **Foundry User** | Foundry **resource** (account) | Read, create, and interact with agents in any project under this resource |
| Agent creators / publishers | **Foundry Project Manager** | Foundry **resource** (account) | Create projects, publish Agent Applications, assign the Foundry User role to others |

> Assign **Foundry User at the resource scope**, not the project scope.
> Resource-scope assignments inherit to every project beneath it, which
> is simpler and matches the docs' recommended minimum.

Without the resource-scope Foundry User role you will see:

> Identity does not have permissions for
> Microsoft.MachineLearningServices/workspaces/agents/read

Without Foundry Project Manager you will see:

> Identity does not have permissions for
> Microsoft.MachineLearningServices/workspaces/agents/action

> **Do not use** `Cognitive Services *` roles for Foundry scenarios.
> The official docs explicitly say those roles are designed for
> accessing AI Services resources directly and don't apply to Foundry.

```powershell
# Get your principal ID
az ad signed-in-user show --query id -o tsv

# Foundry User on the resource scope (minimum for all users)
az role assignment create `
  --assignee-object-id <principal-id> `
  --assignee-principal-type User `
  --role "Foundry User" `
  --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<foundry-resource>

# Foundry Project Manager on the resource scope (agent creators / publishers)
az role assignment create `
  --assignee-object-id <principal-id> `
  --assignee-principal-type User `
  --role "Foundry Project Manager" `
  --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<foundry-resource>
```

> **Tip — use role GUIDs** in scripts to avoid issues during the
> Foundry role-rename rollout:
> Foundry User `53ca6127-db72-4b80-b1b0-d745d6d5456d`,
> Foundry Project Manager `eadc314b-1a2d-4efa-be10-5d325db5065e`.

Assign the roles after the Foundry resource exists but before you try
to open, load, create, or publish agents.

If you used `azd up` (Path B), the subscription, resource group, and
resource name are in the `azd env get-values` output.

See the [Foundry RBAC reference](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry)
for the full role matrix.

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
   `AZURE_OPENAI_DEPLOYMENT_NAME`, and a few others directly into `.env`.
5. Fetch the Azure OpenAI key separately (Bicep does not output secrets):

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
6. Run `samples/hello-foundry-py/app.py` to confirm the model deployment is
   reachable from code.
7. In the [Foundry portal](https://ai.azure.com), open the project and
   create a prompt agent against the `gpt-4.1-mini` deployment
   (steps 2–4 of Path A). Add `FOUNDRY_AGENT_NAME=<agent-name>` to `.env`.
8. Run `samples/hello-agent-py/app.py` to confirm the agent wiring.

## Success criterion

The deployed version should be easy to explain, easy to refresh, and easy to
show to a live audience. If you can hit refresh and re-run the demo cleanly
on stage, you are in good shape.

## When you outgrow this deployment

For richer orchestration, Azure-platform deployment patterns, governance,
and other directions beyond the spark, see `docs/05-going-further.md`.
