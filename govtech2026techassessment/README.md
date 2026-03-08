# govtech2026techassessment

## 1) Introduction and Approach Overview
This repository contains a complete take-home submission for designing a GenAI support chatbot for a university marketplace.

My approach:
- Design a policy-aware system prompt first (`prompt.md`) to set behavior boundaries.
- Define measurable golden tests (`test-cases.json`) that reflect real campus marketplace operations.
- Document a repeatable testing process (`testing-framework.md`) and sample output (`testing-result.md`).
- Propose a controlled prompt update lifecycle (`update-process.md`, `automation-concept.py`) with rollback.
- Capture domain-specific product risks and seasonal behavior (`marketplace-insights.md`).

## 2) How to Review This Submission
1. Read `prompt.md` for chatbot behavior specification.
2. Read `prompt-analysis.md` for rationale behind prompt decisions.
3. Inspect `test-cases.json` for breadth and structure of golden tests.
4. Review `testing-framework.md` for execution method and quality gates.
5. Check `testing-result.md` for sample evaluation artifacts.
6. Read `update-process.md` and `automation-concept.py` for deployment governance.
7. Read `marketplace-insights.md` for domain-specific requirements.
8. Read `Sample-Chatbot-info.md` for prototype platform choice and deployment notes.
9. Read `PROCESS_LOG.md` for effort timeline and decision trail.

## 3) Assumptions About the University Marketplace
- Access is restricted to verified students/alumni/staff with institutional email.
- Payment is peer-to-peer (PayNow, cash, campus wallet) and happens outside platform escrow.
- Pickup is primarily on-campus (library, dorm lobby, student union) with optional meet-up safety tips.
- Moderation team exists during business hours, with after-hours incident queueing.
- The chatbot is a support assistant, not a transactional agent that directly executes payments.

## 4) Time Breakdown (2.75 hours total)
- Prompt design and analysis: 50 minutes
- Golden test design and JSON authoring: 70 minutes
- Testing framework + result artifact: 30 minutes
- Update process + automation concept: 25 minutes
- Marketplace insights: 20 minutes
- Prototype documentation: 15 minutes
- Packaging and review: 15 minutes

## 5) Next Steps for a Real Project
- Integrate with real moderation/event logs and build live regression dashboards.
- Add retrieval over policy docs and FAQ to reduce hallucination risk.
- Add multilingual support and localization for international students.
- Introduce A/B testing for response style and escalation thresholds.
- Run red-team safety tests for scam and harassment scenarios before production.

## 6) Personal Reflection (Most Challenging Component)
The hardest part was balancing concise user-friendly responses with strict policy enforcement and escalation logic. In practice, over-restrictive prompts degrade user experience, while permissive prompts create safety risk. The final design uses explicit conditional routing and a consistent output schema to keep this balance testable.

## 7) Three Alternative Approaches Considered and Rejected
1. **Single generic support prompt without role-specific logic**
   - Rejected because buyer/seller/safety intents need different handling depth and escalation behavior.
2. **Pure rule-based chatbot (no LLM)**
   - Rejected due to poor handling of ambiguous and multi-intent student queries.
3. **LLM-only with no structured output schema**
   - Rejected because it makes testing and regression comparisons difficult.

## 8) My Experience with University Marketplaces
- **Buyer perspective:** Frequent need for trust signals (seller credibility, item condition proofs, clear pickup details).
- **Seller perspective:** High message volume, no-shows, and repetitive negotiation requests are common pain points.
- This informed test coverage around disputes, scams, listing quality, and pickup coordination.

## 9) Repository Contents
- `prompt.md`
- `prompt-analysis.md`
- `test-cases.json`
- `testing-framework.md`
- `testing-result.md`
- `update-process.md`
- `automation-concept.py`
- `marketplace-insights.md`
- `Sample-Chatbot-info.md`
- `PROCESS_LOG.md`
- `resources/`
