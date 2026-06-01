import os

# Minimal placeholder sample for a Foundry Agent Service call.
# Replace this with your real SDK usage when you are ready to test the live flow.

PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT", "")
AGENT_NAME = os.getenv("FOUNDRY_AGENT_NAME", "")

print("Agent sample ready.")
print(f"Project endpoint configured: {'yes' if PROJECT_ENDPOINT else 'no'}")
print(f"Agent name configured: {'yes' if AGENT_NAME else 'no'}")
