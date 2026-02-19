from __future__ import annotations

import json
import os
from typing import Any, Dict, Optional

from openai import OpenAI
from pydantic import ValidationError

from a11y_bot.schemas import AccessibilityReviewResponse
from a11y_bot.utils import (
    ensure_score_breakdown,
    normalize_issue_ids,
    parse_markdown_structure,
    truncate_text,
    try_parse_json,
)

SYSTEM_PROMPT = (
    "You are an accessibility expert for educational content. "
    "Review Markdown content contextually and pragmatically, not as a blind checklist. "
    "Prioritize custom rules when they conflict with general best practices. "
    "Output STRICT JSON only, with no markdown fences or extra text."
)


def build_professor_report(result: AccessibilityReviewResponse) -> str:
    lines = [
        "# Accessibility Review Report",
        "",
        f"## Overall Score: {result.score}/100",
        "",
        "## Quick Summary",
    ]

    for bullet in result.summary_bullets:
        lines.append(f"- {bullet}")

    lines.extend(["", "## Findings"])
    if not result.issues:
        lines.append("- No accessibility issues were identified in this review.")
    else:
        for issue in result.issues:
            lines.extend(
                [
                    f"### {issue.id} - {issue.title} ({issue.severity.upper()})",
                    f"Why it matters: {issue.explanation}",
                    f"Evidence: {issue.evidence}",
                    f"Suggested fix: {issue.suggestion}",
                    "",
                ]
            )

    lines.extend(["## Scoring Details", f"- Base score: {result.score_breakdown.base}"])
    for p in result.score_breakdown.penalties:
        lines.append(
            f"- {p.severity.title()}: {p.count} x {p.penalty_per_item} = -{p.subtotal}"
        )
    lines.append(f"- Final score: {result.score_breakdown.final}")

    if result.applied_rules:
        lines.extend(["", "## Applied Custom Rules", result.applied_rules])

    return "\n".join(lines).strip() + "\n"


def review_markdown_accessibility(
    markdown_text: str,
    rules_text: Optional[str],
    model: str,
    temperature: float = 0.2,
) -> AccessibilityReviewResponse:
    if not markdown_text.strip():
        return _empty_doc_response(rules_text)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set.")

    parsed = parse_markdown_structure(markdown_text)
    client = OpenAI(api_key=api_key)

    user_prompt = _build_user_prompt(markdown_text, rules_text, parsed.__dict__)

    raw_text = _call_llm(
        client=client,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
        temperature=temperature,
    )

    payload = try_parse_json(raw_text)
    if payload is None:
        retry_prompt = (
            user_prompt
            + "\n\nYour previous response was not valid JSON. "
            "Return only valid JSON matching the required schema."
        )
        raw_text = _call_llm(
            client=client,
            model=model,
            system_prompt=SYSTEM_PROMPT,
            user_prompt=retry_prompt,
            temperature=0.0,
        )
        payload = try_parse_json(raw_text)

    if payload is None:
        raise RuntimeError("Model response was not valid JSON after one retry.")

    payload = _postprocess_payload(payload)

    try:
        return AccessibilityReviewResponse.model_validate(payload)
    except ValidationError as exc:
        raise RuntimeError(f"Model JSON failed schema validation: {exc}") from exc


def _call_llm(
    client: OpenAI,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
) -> str:
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content or ""


def _build_user_prompt(
    markdown_text: str,
    rules_text: Optional[str],
    parsed_structure: Dict[str, Any],
) -> str:
    output_schema = {
        "score": "integer 0-100",
        "score_breakdown": {
            "base": 100,
            "penalties": [
                {
                    "severity": "high|medium|low",
                    "count": "int",
                    "penalty_per_item": "int",
                    "subtotal": "int",
                }
            ],
            "final": "int",
        },
        "summary_bullets": ["3-6 concise bullets"],
        "issues": [
            {
                "id": "ISSUE-1",
                "severity": "low|medium|high",
                "title": "short",
                "explanation": "1-3 educator-friendly sentences",
                "evidence": "snippet or reference",
                "suggestion": "specific actionable fix",
            }
        ],
        "applied_rules": "optional string",
    }

    rules_section = rules_text.strip() if rules_text else "No custom rules provided."

    return (
        "Review this Markdown document for accessibility issues. "
        "Use context-aware judgment. Missing alt text is only an issue when context suggests an informative image, "
        "and may be acceptable if decorative and explicitly indicated or already fully described nearby.\n\n"
        "Tasks:\n"
        "1) Identify accessibility issues with severity\n"
        "2) Explain impact for assistive technologies and cognitive accessibility\n"
        "3) Suggest concrete improvements (include example alt text when relevant)\n"
        "4) Provide score from 0-100 with transparent penalty breakdown\n\n"
        "Custom Rules (prioritize if conflicts):\n"
        f"{truncate_text(rules_section, 4000)}\n\n"
        "Extracted Markdown Structure:\n"
        f"{json.dumps(parsed_structure, indent=2)}\n\n"
        "Markdown Content:\n"
        f"{truncate_text(markdown_text, 12000)}\n\n"
        "Return JSON EXACTLY with this shape:\n"
        f"{json.dumps(output_schema, indent=2)}\n"
        "No extra keys. No markdown code fences."
    )


def _postprocess_payload(payload: dict) -> dict:
    payload = dict(payload)

    if "issues" not in payload or not isinstance(payload["issues"], list):
        payload["issues"] = []
    payload["issues"] = normalize_issue_ids(payload["issues"])

    if "summary_bullets" not in payload or not isinstance(payload["summary_bullets"], list):
        payload["summary_bullets"] = []

    if len(payload["summary_bullets"]) < 3:
        payload["summary_bullets"] = (
            payload["summary_bullets"]
            + [
                "Review completed with context-aware checks.",
                "Address high-severity issues first for greatest accessibility impact.",
                "Re-run review after edits to confirm score improvement.",
            ]
        )[:3]

    if len(payload["summary_bullets"]) > 6:
        payload["summary_bullets"] = payload["summary_bullets"][:6]

    if payload.get("score_breakdown", {}).get("base") != 100:
        payload = ensure_score_breakdown(payload)
    else:
        payload = ensure_score_breakdown(payload)

    return payload


def _empty_doc_response(rules_text: Optional[str]) -> AccessibilityReviewResponse:
    applied_rules = None
    if rules_text and rules_text.strip():
        applied_rules = "Custom rules were provided but the document was empty, so no rule-based checks were applied."

    payload = {
        "score": 100,
        "score_breakdown": {
            "base": 100,
            "penalties": [
                {"severity": "high", "count": 0, "penalty_per_item": 15, "subtotal": 0},
                {"severity": "medium", "count": 0, "penalty_per_item": 8, "subtotal": 0},
                {"severity": "low", "count": 0, "penalty_per_item": 3, "subtotal": 0},
            ],
            "final": 100,
        },
        "summary_bullets": [
            "The uploaded Markdown document is empty.",
            "No accessibility issues were detected because there was no content to evaluate.",
            "Add content and run the review again for a meaningful assessment.",
        ],
        "issues": [],
        "applied_rules": applied_rules,
    }

    return AccessibilityReviewResponse.model_validate(payload)
