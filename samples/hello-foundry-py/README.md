# hello-foundry-py

A tiny sample for validating a Foundry model call.

## What to do

1. Copy `.env.sample` from the repo root to `.env`.
2. Fill in `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, and `AZURE_OPENAI_DEPLOYMENT_NAME`.
3. Install dependencies:
   - **Windows:** `py -3.12 -m pip install -r requirements.txt`
   - **macOS / Linux:** `python3 -m pip install -r requirements.txt`
4. Run the sample (from the repo root):

   ```powershell
   py -3.12 samples/hello-foundry-py/app.py
   ```

   ```bash
   python3 samples/hello-foundry-py/app.py
   ```

## Expected result

You should see a real chat completion from your Azure OpenAI deployment, not just a placeholder message.
