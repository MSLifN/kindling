# Get set up with Foundry Toolkit

Foundry Toolkit is the "build half" of Kindling: GitHub Copilot writes
the code, Foundry Toolkit gives you the models and agent surface to
call from it. It's a single VS Code extension that covers the full AI
app workflow — discover models, deploy them, test prompts in a
playground, build agents, and monitor everything — locally or in the
cloud.

Official docs:

- [Foundry Toolkit overview](https://code.visualstudio.com/docs/intelligentapps/overview)
- [Working with the extension](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/get-started-projects-vs-code)
- [Copilot tools for agent development](https://code.visualstudio.com/docs/intelligentapps/copilot-tools)
- [Azure AI Foundry Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)

---

## 1 — Install the extension

1. Install the [.NET Runtime](https://learn.microsoft.com/en-us/dotnet/core/install/)
   (required dependency).
2. Install the extension:
   [Foundry Toolkit for VS Code](vscode:extension/ms-windows-ai-studio.windows-ai-studio)
   (ID: `ms-windows-ai-studio.windows-ai-studio`).
3. The Foundry Toolkit icon appears in the Activity Bar.
4. **Local models (optional):** `F1` →
   `Foundry Toolkit: Install environment prerequisites` to set up
   [Foundry Local](https://www.foundrylocal.ai/). Verify with
   `Foundry Toolkit: Validate environment prerequisites`.

## 2 — Azure prerequisites

Before you connect Foundry Toolkit to Azure, make sure resource
providers are registered and your identity has the right roles.

### Register resource providers (once per subscription)

```powershell
az provider register --namespace Microsoft.CognitiveServices --wait
az provider register --namespace Microsoft.MachineLearningServices --wait
```

Verify:

```powershell
az provider show --namespace Microsoft.CognitiveServices --query registrationState -o tsv
az provider show --namespace Microsoft.MachineLearningServices --query registrationState -o tsv
```

Both should return `Registered`. You need at least Contributor on the
subscription to register them — ask your coordinator if you don't have
it.

### Grant the right Foundry roles

The [official RBAC reference](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry)
defines two key roles.

| Who | Role | Scope | Lets you… |
|---|---|---|---|
| Every participant | **Foundry User** | Foundry **resource** (account) | Read, create, and interact with agents in any project under this resource |
| Agent creators / publishers | **Foundry Project Manager** | Foundry **resource** (account) | Create projects, publish Agent Applications, assign the Foundry User role to others |

> Assign at the **resource** scope, not the project scope — it
> inherits to every project beneath it.

```powershell
# Get your principal ID
az ad signed-in-user show --query id -o tsv

# Foundry User (minimum for all users)
az role assignment create `
  --assignee-object-id <principal-id> `
  --assignee-principal-type User `
  --role "Foundry User" `
  --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<foundry-resource>

# Foundry Project Manager (agent creators / publishers)
az role assignment create `
  --assignee-object-id <principal-id> `
  --assignee-principal-type User `
  --role "Foundry Project Manager" `
  --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<foundry-resource>
```

> **Tip — use role GUIDs** in scripts to avoid issues during the
> Foundry role-rename rollout:
> Foundry User `53ca6127-db72-4b80-b1b0-d745d6d5456d`,
> Foundry Project Manager `eadc314b-1a2d-4efa-be10-5d325db5065e`.

Without the right roles you'll see errors like
`agents/read` (needs Foundry User) or `agents/action`
(needs Foundry Project Manager).

> **Do not use** `Cognitive Services *` roles for Foundry scenarios —
> the official docs say those don't apply.

## 3 — Connect and deploy your first model

### Sign in

1. Click the **Azure** icon → **Sign in to Azure…**
2. Expand your subscription → resource group → **Foundry**.
3. Right-click your project → **Open in Foundry Toolkit Extension**.

No project yet? Click **+ Create Project** in the **My Resources**
section, pick (or create) a resource group and location, and name the
project. A popup lets you deploy a model immediately.

### Deploy a model

1. Open the Model Catalog (`F1` → `Foundry Toolkit: Show model catalog`).
2. Find a model and click **Deploy** → enter a deployment name, type,
   version, and optional TPM limit → **Deploy in Foundry**.
3. The model appears under **Models** in your project. Click it to see
   the endpoint URI and auth key.

### Try it in the playground

Right-click the deployed model → **Open in playground** (or
double-click **Model Playground** in Developer Tools). Type a prompt,
review the output, and click **View code** (top-right) to see the
programmatic equivalent.

### Generate sample code

Right-click the deployed model → **Open code file** → choose SDK,
language, and auth method. A ready-to-run file opens in a new tab.

## 4 — Know the sidebar

The extension view has three sections. Everything you just did above
lives inside them.

| Section | What's inside |
|---|---|
| **My Resources** | **Local Resources** (local models, agents, tools) · **Your Foundry Project** (deployed models, prompt agents, workflows, hosted agents, MCP tools, knowledge/vector stores) · **Connected Resources** (GitHub models and other providers) |
| **Developer Tools** | **Discover** — Model Catalog, Tool Catalog · **Build** — Create Agent, Agent Builder, Agent Inspector, Deploy to Foundry, Hosted Agent Playground, Model Playground, Model Conversion, Fine-tuning · **Monitor** — Tracing, Evaluation, Model Profiling (Windows ML) |
| **Help & Feedback** | Docs, release notes, issue reporting, community |

Use `F1` → search **Foundry Toolkit** to see every available command.

### Feature highlights

| Feature | What it does |
|---|---|
| **Model Catalog** | Browse models from Microsoft Foundry, Foundry Local, GitHub, ONNX, Ollama, OpenAI, Anthropic, Google. Compare side-by-side. |
| **Playground** | Interactive chat with prompts, parameters, multi-modal inputs. |
| **Agent Builder** | Prompt engineering, MCP tool integration, production-ready code generation. |
| **Agent Inspector** | Debug and visualize agents inside VS Code. |
| **Tool Catalog** | Connect Foundry and local MCP server tools to your agents. |
| **Evaluation** | Assess models with built-in evaluators (F1, relevance, similarity, coherence) or custom criteria. |
| **Tracing** | Collect and visualize trace data for AI app performance. |
| **Fine-tuning** | Train models locally (GPU) or in the cloud (Azure Container Apps). |
| **Model Conversion** | Convert, quantize, optimize models for CPU/GPU/NPU. |

## 5 — Copilot tools for agent development

Foundry Toolkit extends GitHub Copilot's **Agent mode** with four
tools that VS Code can invoke automatically. Open Chat (`Ctrl+Alt+I`),
select **Agent**, and click **Configure Tools…** to see them.

| Tool | What it does | Try this prompt |
|---|---|---|
| **Agent Code Gen** | Generates agent code from a description. Defaults to the Microsoft Agent Framework SDK and GPT-4.1. Supports function calling, MCP, streaming, and workflow patterns (sequential, switch-case, loop, human-in-the-loop). | `Create an AI app that helps me manage travel queries.` |
| **AI Model Guide** | Recommends the best model for your use case with details on context length, cost, and quality/speed/safety metrics. Also activates during code gen. | `Which models are designed for reasoning or math tasks?` |
| **Evaluation Code Gen** | Scaffolds evaluation code using the Azure AI Eval SDK — suggests metrics, generates synthetic queries, runs batch tests. | `Create an evaluation that assesses response accuracy for my travel assistant.` |
| **Tracing Code Gen** | Adds tracing best practices. Supports Python (agent-framework, openai, langchain, etc.) and JS/TS (openai, langchain, anthropic, etc.). | `Enable tracing for my agent-framework app in Python.` |

Two **Foundry Skills** also activate automatically in Copilot chat
when the conversation context calls for them:

- **microsoft-foundry-agent-framework-code-gen** — scaffolds and
  enhances agent apps.
- **microsoft-foundry** — deploys, evaluates, and manages Foundry
  resources end-to-end.

## 6 — Kindling-specific tips

- Deploy **`gpt-4.1-mini`** (Global Standard, capacity 1) — it's
  cheap, fast, and matches the Bicep default in `infra/main.bicep`.
- Use the **Playground** to iterate on a system prompt before pasting
  it into the agent in the Foundry portal.
- Copy the deployment name and endpoint from the **Models** view into
  `.env` — those two values are what
  `samples/hello-foundry-py/app.py` reads.
- Agent authoring lives in the Foundry portal at
  https://ai.azure.com — jump there when the toolkit doesn't yet
  expose the feature you need.

### Troubleshooting

| Problem | Fix |
|---|---|
| Extension doesn't appear after install | Restart VS Code; verify it's enabled in the Extensions view. |
| Sign-in fails / subscriptions don't load | Check Azure account permissions; sign out and back in. |
| Model deployment fails with quota error | Check subscription quota; request an increase or delete unused deployments. |
| `agents/read` permission error | Grant **Foundry User** at the Foundry resource scope (see section 2). |
| `agents/action` permission error | Grant **Foundry Project Manager** at the Foundry resource scope (see section 2). |

## Further reading

- [Adding generative AI models](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Agent Builder](https://code.visualstudio.com/docs/intelligentapps/agentbuilder) and [Agent Inspector](https://code.visualstudio.com/docs/intelligentapps/agent-inspector)
- [Copilot tools deep-dive](https://code.visualstudio.com/docs/intelligentapps/copilot-tools)
- [Foundry RBAC reference](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry)

---

**Next step →** `docs/03-deploy-easiest-path.md` — build and deploy
your agent.
