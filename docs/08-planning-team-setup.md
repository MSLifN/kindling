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
