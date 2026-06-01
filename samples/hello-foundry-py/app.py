import os

# Minimal placeholder sample for a Foundry model call.
# Replace this with your real SDK usage when you are ready to test the live flow.

MODEL_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")

print("Foundry sample ready.")
print(f"Endpoint configured: {'yes' if MODEL_ENDPOINT else 'no'}")
print(f"Deployment configured: {'yes' if DEPLOYMENT_NAME else 'no'}")
