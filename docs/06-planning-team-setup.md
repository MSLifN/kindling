# Planning team setup

Use this guide when you need to prepare a shared Foundry + Azure environment for a hackathon or live demo session.

## Recommended baseline

Pre-create the following shared resources before participants arrive:

- one Foundry resource and one Foundry project
- one default chat model deployment
- one optional embedding deployment if RAG or semantic search will be used
- one starter agent in the project
- one Application Insights / Log Analytics workspace
- one storage account only if file-based demos are needed

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
5. If you're sharing one Foundry project across teams, you only need
   quota for one deployment. If each team gets their own project (cleaner
   for grading and cleanup), multiply accordingly.

## Recommended access model

Give participants access to the shared project and model, not the whole subscription.

### Minimum access for most participants

- Foundry User on the Foundry project/resource scope
- Cognitive Services OpenAI User on the Azure OpenAI resource
- Reader on the monitoring resource

### Deeper access for advanced participants

- Foundry Project Manager on the Foundry resource scope
- Cognitive Services OpenAI Contributor on the Azure OpenAI resource

## Practical rule of thumb

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

- **Shared resources, you provide the values** — send each team
  the three values they need: `FOUNDRY_PROJECT_ENDPOINT`,
  `FOUNDRY_AGENT_NAME`, and `AZURE_OPENAI_API_KEY` (plus
  `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT_NAME` if
  you want them to call the model directly). Tell them to paste
  those into `.env` and skip Path B in
  `docs/03-deploy-easiest-path.md` entirely.
- **Self-serve, each team uses their own subscription** — say so
  clearly. They will follow Path A or Path B in
  `docs/03-deploy-easiest-path.md`.
- **Mixed** — say which teams get which, ideally before the event.
  A team that discovers mid-hackathon that they need their own
  subscription usually does not ship a demo.
