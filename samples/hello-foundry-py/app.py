"""Validate the Kindling kit's Azure OpenAI wiring.

Reads AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, and
AZURE_OPENAI_DEPLOYMENT_NAME from .env, then sends a single chat
completion request to your deployed model and prints the reply.

If this script prints a model response, your direct model-call path
works end to end.
"""

import os
import sys

try:
    from dotenv import load_dotenv
    from openai import AzureOpenAI
except ImportError as exc:
    print("Missing dependency: run 'pip install -r requirements.txt' first.")
    sys.exit(1)


def main() -> None:
    load_dotenv()
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "").strip()
    api_key = os.getenv("AZURE_OPENAI_API_KEY", "").strip()
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "").strip()

    missing = [name for name, value in {
        "AZURE_OPENAI_ENDPOINT": endpoint,
        "AZURE_OPENAI_API_KEY": api_key,
        "AZURE_OPENAI_DEPLOYMENT_NAME": deployment_name,
    }.items() if not value]

    if missing:
        print("Missing required environment variables:", ", ".join(missing))
        print("Copy .env.sample to .env and fill in your Azure OpenAI values first.")
        sys.exit(1)

    try:
        client = AzureOpenAI(
            api_key=api_key,
            azure_endpoint=endpoint,
            api_version="2024-10-21",
        )

        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are validating the Kindling starter kit."},
                {"role": "user", "content": "Reply in one sentence that the Kindling sample is working."},
            ],
            temperature=0.2,
            max_tokens=80,
        )

        content = response.choices[0].message.content or "(no response returned)"
        print("Foundry sample response:")
        print(content)
    except Exception as exc:
        print("Foundry sample failed:", exc)
        print("Verify your Azure OpenAI endpoint, key, deployment name, and region.")
        sys.exit(1)


if __name__ == "__main__":
    main()
