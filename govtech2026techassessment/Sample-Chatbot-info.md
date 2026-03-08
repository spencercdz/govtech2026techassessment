# Sample Chatbot Prototype Info

## Platform Selected
**Poe**

## Why This Platform
- Fastest path to deploy and share a working chatbot via public URL.
- Low setup overhead for prompt iteration during take-home timelines.
- Good fit for demonstrating prompt behavior, safety guardrails, and support workflows.
- Easy evaluator access without requiring local setup.

## Access URL
- Prototype URL: [CampusMarket on Poe](https://poe.com/CampusMarket)

## Prototype Design
- Core behavior implemented using `prompt.md` as the system instruction baseline.
- Inputs: user message + lightweight context assumptions (buyer/seller/new user/safety intent).
- Output style: structured, action-oriented responses aligned to the testing rubric.
- Safety handling: high-risk intents route to clear escalation guidance (moderator/campus safety).

## Testing Performed
- Golden test simulation designed against `test-cases.json`.
- Evaluation rubric and pass gates documented in `testing-framework.md`.
- Sample run artifact recorded in `testing-result.md`.

## Assumptions
- Poe-hosted prototype demonstrates conversational behavior but does not directly integrate with internal university moderation APIs.
- Account verification, payments, and case management remain conceptual or manual in this prototype stage.

## Limitations
- No direct backend integration with production marketplace databases.
- No live moderation workflow ingestion or case-status sync.
- Prototype behavior may vary with platform-level model updates over time.
