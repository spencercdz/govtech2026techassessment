# Prompt Analysis

I revised the system prompt using the structure recommended in OpenAI's official prompt engineering guidance: clear identity, explicit instructions, examples, and context boundaries. The updated prompt now has a strict instruction-priority stack (safety, policy, task completion, style), a defined input contract, and explicit routing for buyer/seller/new-user/safety scenarios. This follows the "write clear instructions" and "use structured formatting with Markdown/XML" principles so the model behavior is easier to control and audit.

To improve reliability, I added a hard output contract requiring valid JSON with fixed keys and constrained enums (`risk_level`, `escalation`). This supports deterministic evaluation in golden tests and reduces formatting drift. I also added two few-shot examples because the guidance emphasizes examples as a strong way to anchor output patterns. Together with a response quality checklist, this makes the prompt more robust for production-style regression testing.

For safety, the prompt includes explicit refusal rules and a severity-based escalation matrix (`P0-P3`) mapped to concrete actions. This aligns with best-practice recommendations to constrain unsafe outputs and provide predictable policy-compliant behavior under adversarial or risky inputs. University-specific context (semester spikes, dorm logistics, exam-period coordination) is preserved so the assistant remains domain-appropriate rather than generic.

Reference used: [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering/system-prompts)
