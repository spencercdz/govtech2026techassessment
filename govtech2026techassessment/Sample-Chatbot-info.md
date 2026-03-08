# Sample Chatbot Prototype Info

## Platform Selected
**Flowise (open-source)**

## Why This Platform
- Fast visual orchestration for prompt + policy layers.
- Easy integration of guardrail nodes and webhook-based escalation.
- Suitable for quick prototype delivery within the assessment timeline.
- Can be self-hosted or deployed on free-tier infrastructure.

## Access URL
- Prototype URL: `Not published from this offline environment`
- Suggested deployment target: Render/Railway with Flowise cloud URL after publish.

## Prototype Design
- Core behavior implemented using `prompt.md` as system prompt.
- Inputs: user message + lightweight context tags (role hint, account state).
- Output: structured JSON-style response for easier testing.
- Safety branch routes high-risk intents to moderation escalation template.

## Testing Performed
- Golden test simulation against `test-cases.json`.
- Output scoring approach documented in `testing-framework.md`.
- Sample run artifact recorded in `testing-result.md`.

## Assumptions
- Real policy API and moderation queue were not available; mocked as logical pathways.
- Authentication and profile data are represented as context variables only.

## Limitations
- No live backend integrations (payments, user database, moderation case system).
- No production telemetry from real user traffic.
- URL publication not completed in this execution environment.
