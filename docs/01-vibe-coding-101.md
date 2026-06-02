# Fast prototyping with GitHub Copilot

In a hackathon you have hours, not weeks. The job of this kit is to
shorten the loop between "I have an idea" and "I can show it on a
screen." GitHub Copilot is the main accelerator.

The canonical guidance lives with GitHub:

- [GitHub Copilot best practices](https://docs.github.com/en/copilot/get-started/best-practices)
  — how to write good prompts, when to accept a suggestion, when to
  iterate, and how to keep context tight.

## Kindling-specific tips

- **Start with one user problem from `starter-ideas/`.** Don't pick
  a theme; pick a sentence ("I never read meeting summaries").
- **Switch to the kindling agent in GitHub Copilot Chat** to frame the
  idea before you ask GitHub Copilot to write code. The custom agent in
  `.github/agents/kindling.agent.md` is tuned for the first 15 minutes.
- **Validate the wiring first.** Run `samples/hello-foundry-py/app.py`
  before you ask GitHub Copilot for the real feature — it removes the
  whole "is my `.env` right?" debugging detour from your hackathon day.
- **Keep the first version visible.** A printed JSON blob in a terminal
  beats a half-built UI every time. Make the win obvious in one screen.

If you can explain the result in one sentence and show it in one
screen, you are in good shape.
