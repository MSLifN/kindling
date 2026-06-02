# Planning team setup

Use this guide when you need to prepare a shared Foundry + Azure environment for a hackathon or live demo session.

## Recommended baseline

Pre-create the following before participants arrive.

**Once per event (shared across all teams):**

- one Foundry resource (account) in your chosen region
- one chat model deployment (e.g. `gpt-4.1-mini` GlobalStandard) on
  the Foundry resource — model deployments live at the Foundry **account** scope,
  so every team's project references the same deployment
- one optional embedding deployment if RAG or semantic search will be used
- one Application Insights / Log Analytics workspace
- one storage account only if file-based demos are needed

**Per team:**

- one Foundry **project** inside the shared Foundry resource —
  isolates each team's agents, threads, evaluations, and role
  assignments. Much easier to grade and clean up afterwards than a
  shared project.
- one starter agent inside that team's project (optional — most teams
  replace it on day one)

## Model deployment quota — request early

This is the single thing most likely to break a hackathon day. Each Foundry
project uses Azure OpenAI quota measured in **thousands of tokens per
minute (TPM)** per region per subscription. With ten teams hitting
`gpt-4.1-mini` GlobalStandard in the same region, default quota disappears
fast.

Before the event:

1. Decide which region the event uses (EU teams: `swedencentral`; US
   teams: `eastus2`).
2. Estimate worst-case TPM: number of teams × peak rate per team.
   For a hackathon, 10 TPM per team is usually enough for `gpt-4.1-mini`.
3. Check current quota with:
   ```bash
   az cognitiveservices usage list --location <region>
   ```
4. If you're short, [request a quota increase](https://learn.microsoft.com/azure/ai-foundry/openai/quotas-limits#how-to-request-increases-to-the-default-quotas-and-limits)
   at least a week ahead — approval can take days.
5. Because the chat model deployment lives at the Foundry **account**
   scope, all team projects share one quota pool. Size that pool for
   the whole event in one calculation — you do not need to multiply by
   number of teams.

## Recommended access model

Give participants access to the shared project and model, not the whole subscription.

The canonical role list is in the
[Azure AI Foundry RBAC reference](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry).
Assign team roles at each team's **project** scope, not at the
Foundry resource scope, so teams cannot see or modify each other's
agents.

### Minimum access for most participants

- Foundry User on each team's Foundry **project** scope
- Cognitive Services OpenAI User on the Azure OpenAI resource
- Reader on the monitoring resource

### Deeper access for advanced participants

- Foundry Project Manager on each team's Foundry **project** scope
- Cognitive Services OpenAI Contributor on the Azure OpenAI resource

## Practical rule of thumb

Assign all Foundry roles at each team's project scope (not the
Foundry resource scope) so teams cannot see or modify each other's
agents.

If the goal is quick onboarding for everyone, start with:

- Foundry User
- Cognitive Services OpenAI User
- Reader on monitoring resources

If you expect teams to build and iterate more deeply, also add:

- Foundry Project Manager
- Cognitive Services OpenAI Contributor

## Security notes

- Avoid giving everyone Owner unless you truly need that level of access.
- Use Entra groups instead of assigning permissions one by one.
- Grant storage access only when a demo genuinely needs file or blob operations.

## Communicate the access mode to participants

The single most common participant friction is "I have access… to what?"
Decide your model up front and tell every team before the event starts.

- **Shared resources, you provide the values** — each team gets
  their own `FOUNDRY_PROJECT_ENDPOINT` (one per team's project) but
  shares the Azure OpenAI endpoint, deployment name, and key with
  every other team. Send each team their three project-scoped values
  (`FOUNDRY_PROJECT_ENDPOINT`, `FOUNDRY_AGENT_NAME`,
  `AZURE_OPENAI_API_KEY`) plus the shared `AZURE_OPENAI_ENDPOINT` and
  `AZURE_OPENAI_DEPLOYMENT_NAME`. Tell them to paste those into `.env`
  and skip Path B in `docs/03-deploy-easiest-path.md` entirely.
- **Self-serve, each team uses their own subscription** — say so
  clearly. They will follow Path A or Path B in
  `docs/03-deploy-easiest-path.md`.
- **Mixed** — say which teams get which, ideally before the event.
  A team that discovers mid-hackathon that they need their own
  subscription usually does not ship a demo.
