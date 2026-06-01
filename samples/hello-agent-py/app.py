import os
import sys

try:
    from dotenv import load_dotenv
    from azure.ai.projects import AIProjectClient
    from azure.identity import DefaultAzureCredential
except ImportError:
    print("Missing dependency: run 'pip install -r requirements.txt' first.")
    sys.exit(1)


def main() -> None:
    load_dotenv()

    endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT", "").strip()
    agent_name = os.getenv("FOUNDRY_AGENT_NAME", "").strip()

    missing = [k for k, v in {
        "FOUNDRY_PROJECT_ENDPOINT": endpoint,
        "FOUNDRY_AGENT_NAME": agent_name,
    }.items() if not v]
    if missing:
        print("Missing required environment variables:", ", ".join(missing))
        print("Copy .env.sample to .env and fill in your Foundry project values first.")
        sys.exit(1)

    try:
        with (
            DefaultAzureCredential() as credential,
            AIProjectClient(endpoint=endpoint, credential=credential) as project,
            project.get_openai_client() as openai_client,
        ):
            agent = project.agents.get(agent_name=agent_name)
            print(f"Agent retrieved: {agent.name} (id={agent.id})")

            conversation = openai_client.conversations.create()

            response = openai_client.responses.create(
                conversation=conversation.id,
                extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
                input="Reply in one short sentence that the Kindling agent sample is working.",
            )

            print("Agent sample response:")
            print(response.output_text)
    except Exception as exc:
        print("Agent sample failed:", exc)
        print(
            "If this is your first run, sign in with 'az login' and confirm "
            "your Foundry project endpoint and agent name."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
