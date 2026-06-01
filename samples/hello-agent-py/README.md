# hello-agent-py

A tiny sample for validating an agent-service flow against an existing Foundry agent.

## What to do

1. Create or pick an agent in your Microsoft Foundry project and note its name.
2. Copy `.env.sample` from the repo root to `.env`.
3. Fill in `FOUNDRY_PROJECT_ENDPOINT` and `FOUNDRY_AGENT_NAME`.
4. Install dependencies with `py -3.12 -m pip install -r requirements.txt`.
5. Sign in with `az login` (the sample authenticates with `DefaultAzureCredential`).
6. Run the sample:

   ```powershell
   py -3.12 samples/hello-agent-py/app.py
   ```

## Expected result

The script retrieves your agent by name, opens an OpenAI-compatible conversation against the Foundry project, and prints the agent's reply. This confirms your endpoint, identity, and agent reference are wired correctly.
