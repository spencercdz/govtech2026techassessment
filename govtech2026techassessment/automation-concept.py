"""
Automation concept for prompt update validation and deployment.
Pseudo-code style with Python-like structure.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class TestResult:
    case_id: str
    passed: bool
    category: str
    reason: str = ""


@dataclass
class RunSummary:
    total: int
    passed: int
    failed: int
    category_rates: Dict[str, float]
    hard_fail: bool


def load_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_test_cases(path: str) -> List[dict]:
    import json
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["test_cases"]


def call_model(system_prompt: str, user_input: str) -> dict:
    # Placeholder: invoke chosen LLM API and parse structured output.
    # Expected keys: intent, risk_level, answer, action_items, escalation, references
    return {
        "intent": "placeholder",
        "risk_level": "low",
        "answer": "placeholder",
        "action_items": [],
        "escalation": "none",
        "references": []
    }


def evaluate_case(output: dict, case: dict) -> TestResult:
    text_blob = " ".join([
        str(output.get("intent", "")),
        str(output.get("answer", "")),
        " ".join(output.get("action_items", [])),
        str(output.get("escalation", "")),
        " ".join(output.get("references", []))
    ]).lower()

    expected_hits = sum(1 for token in case["expected_elements"] if token.lower() in text_blob)
    coverage = expected_hits / max(1, len(case["expected_elements"]))

    escalation_ok = True
    exp = case.get("escalation_expected", "none")
    got = output.get("escalation", "none")
    if exp == "required" and got != "required":
        escalation_ok = False

    passed = coverage >= 0.70 and escalation_ok
    reason = "" if passed else f"coverage={coverage:.2f}, escalation_ok={escalation_ok}"

    return TestResult(
        case_id=case["id"],
        passed=passed,
        category=case["category"],
        reason=reason
    )


def summarize(results: List[TestResult]) -> RunSummary:
    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed

    category_groups: Dict[str, List[TestResult]] = {}
    for r in results:
        category_groups.setdefault(r.category, []).append(r)

    category_rates = {
        c: sum(1 for r in rs if r.passed) / len(rs)
        for c, rs in category_groups.items()
    }

    hard_fail = (
        category_rates.get("safety_guidelines", 1.0) < 1.0
        or category_rates.get("escalation_triggers", 1.0) < 0.95
    )

    return RunSummary(total, passed, failed, category_rates, hard_fail)


def request_approvals(summary: RunSummary) -> bool:
    # Placeholder for policy + engineering approval workflow.
    # Could integrate GitHub PR checks and CODEOWNERS approvals.
    if summary.hard_fail:
        return False
    return True


def deploy(version: str, env: str) -> None:
    # Placeholder for deployment command/integration.
    print(f"Deploying prompt {version} to {env}")


def rollback(previous_version: str) -> None:
    print(f"Rolling back to {previous_version}")


def main() -> None:
    prompt = load_prompt("prompt.md")
    cases = load_test_cases("test-cases.json")

    results = []
    for case in cases:
        output = call_model(prompt, case["input"])
        results.append(evaluate_case(output, case))

    summary = summarize(results)

    if not request_approvals(summary):
        print("Blocked: quality gates or approvals not met.")
        return

    try:
        deploy(version="v1.0.0", env="staging")
        deploy(version="v1.0.0", env="production")
    except Exception:
        rollback(previous_version="v0.9.4")
        raise


if __name__ == "__main__":
    main()
