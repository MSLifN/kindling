# Citadel governance path

This path is for teams that want to take Kindling from a fast prototype into a more secure, governed, and production-minded AI setup.

## When to use this layer

Use this layer after the basic demo works and before the team tries to scale the idea into a real pilot or shared platform.

## Recommended guidance

1. Keep Kindling as the starting point.
   - Use it to validate the idea quickly.
   - Do not start with Citadel if the team is still proving the concept.

2. Add governance only when the project becomes more than a demo.
   - Introduce runtime policy, cost controls, and traceability.
   - Focus on the parts that reduce security and compliance friction.

3. Treat Citadel as an advanced overlay, not the default onboarding path.
   - Good for teams that want stronger enterprise story and operational maturity.
   - Best used alongside Foundry, azd, and Azure landing-zone thinking.

4. Prioritize the highest-value controls first.
   - Identity and access governance
   - Observability and tracing
   - Policy enforcement at the gateway or agent boundary
   - Cost and usage visibility

## Suggested progression

1. Prototype with Kindling.
2. Deploy with azd and Azure landing-zone patterns.
3. Add Citadel-style governance for secure scaling.
4. Add deeper controls such as the Agent Governance Toolkit when the agent behavior needs stronger runtime enforcement.

## Why this is a good fit

This gives the repo a clear story:
- Kindling = fast spark and experimentation
- Azure landing zone + azd = deployment readiness
- Citadel = governance, observability, and secure scale
