# hello-agent-py

A tiny sample for validating an agent-service flow.

## What to do

1. Copy `.env.sample` from the repo root to `.env`.
2. Fill in `FOUNDRY_PROJECT_ENDPOINT` and `FOUNDRY_AGENT_ID`.
3. Install dependencies with `py -3.12 -m pip install -r requirements.txt`.
4. Sign in with `az login` if your environment uses `DefaultAzureCredential`.
5. Run the sample with:

   ```powershell
   py -3.12 samples/hello-agent-py/app.py
   ```

## Expected result

You should see an agent response from your Foundry project, confirming the agent path is wired correctly.
