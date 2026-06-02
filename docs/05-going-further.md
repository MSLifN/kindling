# Going further

Kindling is a spark, not a platform. When the goal shifts from
"demo this idea" to "ship this idea," explore the projects below.
Each is owned by another team with its own docs — links are starting
points, not promises that the projects stay frozen.

## Build 2026 announcements (June 2026)

The announcements below landed at Microsoft Build 2026 and are directly
relevant to teams using this kit.

### Microsoft Foundry

| What | Status | Why it matters for your hackathon |
|---|---|---|
| **Foundry Toolkit for VS Code** | GA | The extension you installed in [doc 02](02-foundry-toolkit-tour.md) is now generally available. |
| **Hosted agents** | GA expected early July | Managed runtime with sandboxed sessions, state, and filesystem access. Deploy agents built with Agent Framework, Copilot SDK, or LangGraph without rewrites. |
| **Toolboxes** | Public preview | One managed MCP endpoint for every tool type — configure once, point any MCP client at one URL. |
| **Voice Live** | GA (prompt agents) / Preview (hosted) | Add real-time voice to any Foundry agent with a single API. |
| **Agent memory** | Public preview | Procedural, user, and session memory across agent runs. Procedural memory showed +7–14% success-rate gains in Tau-bench. |
| **Foundry IQ** | Available now | Serverless knowledge layer — unifies Work IQ, Fabric IQ, Azure SQL, File Search, and MCP sources behind one retrieval endpoint. |
| **New MAI models** | Public preview | MAI-Thinking-1 (reasoning), MAI-Image-2.5 (image editing), MAI-Transcribe-2 (speech-to-text), MAI-Voice-2 (text-to-speech with cloning). |
| **Agent Framework** | Stable release | Agent harness with skills, memory, middleware. Integrations with Copilot SDK and Claude Agent SDK. Multi-agent orchestration with Magentic-One. |
| **Publish to Teams / M365 Copilot** | GA planned June 2026 | Ship your Foundry agent directly into Teams or Microsoft 365 Copilot with identity and policy flowing through automatically. |
| **ASSERT** | Open source | Policy-driven agent evaluation — converts your policies into measurable evals. Works across LangChain, CrewAI, OpenAI, and more. |
| **Agent Control Specification (ACS)** | Open standard | Portable YAML contract for deterministic safety controls at five agent lifecycle checkpoints. |

Key links:
- [What's new in Microsoft Foundry — Build Edition](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/)
- [Build and run agents at scale](https://aka.ms/BuildFoundryAgents)
- [Foundry IQ announcement](https://aka.ms/FoundryIQ)
- [Developer's guide to model lifecycle management](https://aka.ms/BuildFoundryModels)
- [Build agents you can trust](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/)

### GitHub Copilot

| What | Status | Why it matters for your hackathon |
|---|---|---|
| **Copilot app** | Technical preview (all paid plans) | Desktop home for agent-native dev. Parallel agent sessions, canvases for visible work, voice conversations, cloud sessions. |
| **Copilot SDK** | GA | Embed Copilot's agentic engine in your own apps. Available in TypeScript, Python, Go, .NET, Rust, and Java. |
| **Copilot CLI** | Improved | Rubber duck mode, prompt scheduling, voice input, cloud sessions via `copilot --cloud`. |
| **Cloud & local sandboxes** | Public preview | Isolated execution environments for agent sessions. |
| **Copilot code review for Azure Repos** | Technical preview | Copilot code review now works on Azure DevOps, not just GitHub. |
| **Copilot Memory** | Business & Enterprise | Persistent user preferences across sessions. |
| **MAI-Code-1-Flash** | Available | New fast coding model available in the Copilot model picker. |
| **Gemini models** | Available | Gemini now available in Copilot CLI, cloud agent, and the Copilot app. |
| **Scheduled automations** | Available | Schedule recurring tasks with Copilot cloud agent — no machine needed. |

Key links:
- [GitHub Copilot app — expanded preview](https://github.blog/changelog/2026-06-02-expanded-technical-preview-availability-for-the-github-copilot-app)
- [Copilot SDK GA](https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available)
- [Copilot CLI improvements](https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input)
- [All June 2026 changelog entries](https://github.blog/changelog/2026/)

## Build with more structure

- **Microsoft Agent Framework** — code-first agent orchestration when
  you outgrow prompt-and-tool flows. Good fit when you want a reusable
  app pattern instead of a prompt-only prototype.
  https://github.com/microsoft/agent-framework
  https://learn.microsoft.com/agent-framework/

## Deploy with repeatable infrastructure

- **Azure AI Foundry landing zone + azd** — repeatable deployment,
  environment separation, identity, and connectivity guardrails.
  Use when the goal shifts from local demo to shared environment.
  https://github.com/Azure/AI-Landing-Zones

## Govern at scale

- **Citadel reference architecture** — observability, policy enforcement,
  cost controls, and accountable agent identity for production AI.
  Use when "demo this" becomes "run this safely at scale."
  https://github.com/Azure-Samples/foundry-citadel-platform

- **Agent Governance Toolkit** — in-process runtime policy enforcement
  for sensitive agent actions. Pairs with the Citadel patterns above.
  https://github.com/microsoft/agent-governance-toolkit
  https://microsoft.github.io/agent-governance-toolkit

## Go deeper on GitHub Copilot

GitHub Copilot is the throttle for everything else in this kit. The
links below take you past the basics covered in
`docs/01-vibe-coding-101.md`.

### Learn the fundamentals

- [Develop with GitHub Copilot (Microsoft Learn path)](https://learn.microsoft.com/en-us/training/paths/copilot/)
  — structured modules covering Copilot in IDEs, Chat, and the CLI.
- [GitHub Copilot best practices](https://docs.github.com/en/copilot/get-started/best-practices)
  — prompting patterns, context windows, and when to accept a suggestion.

### Use it everywhere

GitHub Copilot is not just inline completions in VS Code. The same
account works across:

- [GitHub Copilot in the CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli/about-github-copilot-in-the-cli)
  — explain a command, suggest a shell snippet, debug a failed run.
- [GitHub Copilot Chat on mobile](https://docs.github.com/en/copilot/how-tos/use-chat/use-chat-in-mobile)
  — the GitHub Mobile app exposes Copilot Chat against your repos.
- The Foundry Toolkit views in VS Code work side-by-side with Copilot
  Chat, so the same hackathon repo gives you code completion, an AI
  pair, and the model surface in one window.

### Pick the model — and pick the agent

GitHub Copilot now has two layered choices that matter for a
hackathon:

- **Model picker** — switch the model behind Copilot Chat between
  Claude, GPT, Gemini, and others on a per-conversation basis.
  Canonical list:
  [Supported AI models in Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models).
- **Agent HQ** — beyond GitHub's own [Copilot cloud agent](https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent),
  you can opt in to **third-party coding agents** (Anthropic Claude,
  OpenAI Codex) that run inside Copilot on your repos. See the
  February 2026 announcement
  [Pick your agent: use Claude and Codex on Agent HQ](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)
  and the canonical
  [policy reference for third-party coding agents](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies#enabling-or-disabling-third-party-coding-agents-in-your-repositories).
  Third-party coding agents are available on all paid Copilot plans
  but are opt-in per account or organization.

For a hackathon: start with the default model in Chat, then switch
models or agents when you hit something the default handles badly
(e.g. a tricky refactor or a long-running async task).

### Customize and extend

- [github/awesome-copilot](https://github.com/github/awesome-copilot)
  — a community-curated list of custom agents, chat modes,
  instructions, prompts, and extensions for GitHub Copilot. Useful
  when you want to add a domain-specific helper without writing the
  whole agent yourself.
- The custom agents Kindling ships in `.github/agents/` are a small,
  practical example of the same extension surface.
