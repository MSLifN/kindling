# Troubleshooting

## Missing environment variables
If the sample prints that a setting is missing, copy `.env.sample` to `.env` and fill in the values you need.

## Python packages not found
Run one of:

```powershell
py -3.12 -m pip install -r requirements.txt
```

```bash
python3 -m pip install -r requirements.txt
```

## Azure login needed for agent samples
The agent sample uses `DefaultAzureCredential`, so sign in with:

```powershell
az login
```

## Model or agent call fails
Check that:
- the Azure OpenAI endpoint and deployment name are correct
- the Foundry project endpoint is correct
- the agent name (`FOUNDRY_AGENT_NAME`) matches an agent in your Foundry project

## Agent load or publish fails with "does not have permissions"

Two common messages and the fix for each:

| Error contains | Meaning | Fix |
|---|---|---|
| `agents/read` | Cannot open or load agent | Grant **Foundry User** at the Foundry **resource** (account) scope |
| `agents/action` | Cannot create or publish agent | Grant **Foundry Project Manager** at the Foundry **resource** (account) scope |

The [official RBAC reference](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry)
recommends assigning Foundry User at the **resource** scope (not
project scope). Resource-scope assignments inherit to every project
beneath it.

> **Do not use** `Cognitive Services *` roles for Foundry. The docs
> say those roles don't apply to Foundry scenarios.

```powershell
# Get your principal ID
az ad signed-in-user show --query id -o tsv

# Foundry User on resource scope (fixes the read/open error)
az role assignment create `
  --assignee-object-id <principal-id> `
  --assignee-principal-type User `
  --role "Foundry User" `
  --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<foundry-resource>

# Foundry Project Manager on resource scope (fixes the publish error)
az role assignment create `
  --assignee-object-id <principal-id> `
  --assignee-principal-type User `
  --role "Foundry Project Manager" `
  --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<foundry-resource>
```

If the error shows a different object ID than your signed-in account,
use that exact ID as `<principal-id>`. After the role propagates
(usually under a minute), retry the operation.

See `docs/03-deploy-easiest-path.md` (Prerequisites section) for the
full setup, or `docs/06-planning-team-setup.md` if you are an organizer
assigning roles for multiple teams.

## Foundry Toolkit not working or features missing

Foundry Toolkit requires the [.NET Runtime](https://learn.microsoft.com/en-us/dotnet/core/install/). If the extension loads but behaves unexpectedly (greyed-out features, commands not found, sidebar not populating), check whether .NET is installed:

```powershell
dotnet --version
```

If the command is not found, install .NET and restart VS Code.

## Missing resource provider registration

If Azure CLI or the Foundry Toolkit reports that a resource provider is
not registered, register both providers used by Foundry:

```powershell
az provider register --namespace Microsoft.CognitiveServices --wait
az provider register --namespace Microsoft.MachineLearningServices --wait
```

Verify:

```powershell
az provider show --namespace Microsoft.CognitiveServices --query registrationState -o tsv
az provider show --namespace Microsoft.MachineLearningServices --query registrationState -o tsv
```

Both should return `Registered`. You need at least Contributor on the
subscription to register providers — ask your coordinator if you don't
have it.
