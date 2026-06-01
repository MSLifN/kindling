import os
import sys
import time

try:
    from azure.ai.projects import AIProjectClient
    from azure.identity import DefaultAzureCredential
except ImportError as exc:
    print("Missing dependency: run 'pip install -r requirements.txt' first.")
    sys.exit(1)


def main() -> None:
    project_endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT", "").strip()
    agent_id = os.getenv("FOUNDRY_AGENT_ID", "").strip()

    missing = [name for name, value in {
        "FOUNDRY_PROJECT_ENDPOINT": project_endpoint,
        "FOUNDRY_AGENT_ID": agent_id,
    }.items() if not value]

    if missing:
        print("Missing required environment variables:", ", ".join(missing))
        print("Copy .env.sample to .env and fill in your Foundry project values first.")
        sys.exit(1)

    try:
        client = AIProjectClient(
            endpoint=project_endpoint,
            credential=DefaultAzureCredential(),
        )

        agents = client.agents
        agent = agents.get_agent(agent_id)
        thread = agents.create_thread()
        agents.create_message(thread.id, "user", "Reply in one short sentence that the Kindling agent sample is working.")
        run = agents.create_run(thread.id, agent.id)

        while run.status in {"queued", "in_progress"}:
            time.sleep(2)
            run = agents.get_run(thread.id, run.id)

        if run.status != "completed":
            raise RuntimeError(f"Agent run finished with status: {run.status}")

        messages = agents.list_messages(thread.id)
        items = getattr(messages, "data", []) or []
        content = ""
        for item in reversed(items):
            if getattr(item, "role", None) == "assistant":
                text_parts = getattr(item, "content", []) or []
                content = "\n".join(part.text.value for part in text_parts if getattr(part, "type", None) == "text")
                break

        print("Agent sample response:")
        print(content or "(no response returned)")
    except Exception as exc:
        print("Agent sample failed:", exc)
        print("If this is your first run, sign in with 'az login' and confirm your Foundry project endpoint and agent ID.")
        sys.exit(1)


if __name__ == "__main__":
    main()
