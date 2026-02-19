from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional

from reviewer import review_markdown_accessibility
from schemas import AccessibilityReviewResponse


def generate_accessibility_pr_report(
    modified_files: Dict[str, str],
    *,
    rules_text: Optional[str] = None,
    model: str = "gpt-4o-mini",
    temperature: float = 0.2,
    output_dir: str = "./a11y_bot",
)-> None:
    """
    Run accessibility review for each modified file text and write a single Markdown report.

    Args:
        modified_files: Dict where key is filename and value is modified text content.
        rules_text: Optional custom accessibility rules.
        model: OpenAI model name.
        temperature: Sampling temperature for consistency.
        output_dir: Directory where the report file is written.

    Returns:
        None. The report is always written to report.md in output_dir.
    """
    output_path = Path(output_dir).resolve() / "report.md"

    lines = [
        "# Accessibility PR Review",
        "",
        f"- Generated (UTC): {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- Files received: {len(modified_files)}",
        "",
    ]

    if not modified_files:
        lines.extend(
            [
                "## Summary",
                "- No modified files were provided.",
                "",
            ]
        )
        output_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
        return

    per_file_results: list[tuple[str, AccessibilityReviewResponse]] = []
    failed_files: list[tuple[str, str]] = []

    for file_name, modified_text in sorted(modified_files.items(), key=lambda x: x[0].lower()):
        try:
            result = review_markdown_accessibility(
                markdown_text=modified_text or "",
                rules_text=rules_text,
                model=model,
                temperature=temperature,
            )
            per_file_results.append((file_name, result))
        except Exception as exc:
            failed_files.append((file_name, str(exc)))

    lines.extend(_build_overview_section(per_file_results, failed_files))

    for file_name, result in per_file_results:
        lines.extend(_build_file_section(file_name, result))

    if failed_files:
        lines.extend(["## Files With Review Errors", ""])
        for file_name, error_text in failed_files:
            lines.append(f"- `{file_name}`: {error_text}")
        lines.append("")

    output_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return


def _build_overview_section(
    results: list[tuple[str, AccessibilityReviewResponse]],
    failed_files: list[tuple[str, str]],
) -> list[str]:
    lines = ["## Overview", ""]
    if not results:
        lines.append("- No files were successfully reviewed.")
        lines.append("")
        return lines

    total_files = len(results)
    avg_score = round(sum(r.score for _, r in results) / total_files)
    severity_counts = Counter()
    total_issues = 0

    for _, r in results:
        total_issues += len(r.issues)
        for issue in r.issues:
            severity_counts[issue.severity] += 1

    lines.extend(
        [
            f"- Successfully reviewed files: {total_files}",
            f"- Files with review errors: {len(failed_files)}",
            f"- Average score: {avg_score}/100",
            f"- Total issues: {total_issues}",
            (
                "- Severity totals: "
                f"high={severity_counts.get('high', 0)}, "
                f"medium={severity_counts.get('medium', 0)}, "
                f"low={severity_counts.get('low', 0)}"
            ),
            "",
        ]
    )
    return lines


def _build_file_section(file_name: str, result: AccessibilityReviewResponse) -> list[str]:
    lines = [
        f"## File: `{file_name}`",
        "",
        f"- Score: {result.score}/100",
        "",
        "### Summary",
    ]

    for bullet in result.summary_bullets:
        lines.append(f"- {bullet}")

    lines.extend(["", "### Findings"])
    if not result.issues:
        lines.append("- No accessibility issues found.")
    else:
        for issue in result.issues:
            lines.extend(
                [
                    f"- **{issue.id} | {issue.severity.upper()} | {issue.title}**",
                    f"  - Why it matters: {issue.explanation}",
                    f"  - Evidence: {issue.evidence}",
                    f"  - Suggested fix: {issue.suggestion}",
                ]
            )

    lines.extend(["", "### Score Breakdown", f"- Base: {result.score_breakdown.base}"])
    for penalty in result.score_breakdown.penalties:
        lines.append(
            f"- {penalty.severity.title()}: {penalty.count} x {penalty.penalty_per_item} = -{penalty.subtotal}"
        )
    lines.append(f"- Final: {result.score_breakdown.final}")

    if result.applied_rules:
        lines.extend(["", "### Applied Rules", f"- {result.applied_rules}"])

    lines.append("")
    return lines
