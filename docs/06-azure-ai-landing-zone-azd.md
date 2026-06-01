# Azure AI landing zone + azd path

This path is for teams who want to carry the prototype beyond a local demo into a more platform-oriented Azure setup.

## Why this matters

A simple demo is useful, but a stronger platform path gives teams:
- a cleaner Azure deployment story
- a better foundation for security, identity, and environment separation
- a path toward production-style governance without losing the hackathon speed

## Recommended structure

Use this pattern:
- Foundry for the AI runtime and orchestration
- azd for repeatable deployment and environment setup
- Azure AI landing zone concepts for identity, connectivity, and guardrails

## Suggested progression

1. Keep the local demo working.
2. Add an `azd` project structure for repeatable deployment.
3. Use Azure landing-zone thinking for the next phase: governance, environment boundaries, and secure configuration.

## Good fit for this repo

This layer makes Kindling feel more reusable as a real starter kit, not just a time-boxed hackathon artifact.

## Recommended next step: add Citadel-style governance

If the team wants to move beyond a polished prototype, the next useful emphasis is governance and scale:
- use Foundry Control Plane for observability and compliance signals
- add Azure API Management as the AI gateway for policy enforcement and cost control
- wire in Microsoft Entra identity and Agent Identity concepts for accountable agent access
- consider the Agent Governance Toolkit for in-process policy enforcement on sensitive actions

In short: keep Kindling as the fast path, then layer Citadel on top when the goal shifts from "demo this idea" to "run this safely at scale".
