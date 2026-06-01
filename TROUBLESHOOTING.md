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
