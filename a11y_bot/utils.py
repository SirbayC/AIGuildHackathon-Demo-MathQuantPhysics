from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class ParsedMarkdown:
    headings: List[Dict[str, str | int]]
    images: List[Dict[str, str]]
    links: List[Dict[str, str]]
    tables: List[str]
    code_blocks: List[Dict[str, str]]


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.MULTILINE)
IMAGE_RE = re.compile(r"!\[(.*?)\]\((.*?)\)")
LINK_RE = re.compile(r"(?<!!)\[(.*?)\]\((.*?)\)")
CODE_BLOCK_RE = re.compile(r"```([a-zA-Z0-9_-]*)\n(.*?)```", re.DOTALL)


def parse_markdown_structure(markdown_text: str) -> ParsedMarkdown:
    headings = [
        {"level": len(m.group(1)), "text": m.group(2).strip()}
        for m in HEADING_RE.finditer(markdown_text)
    ]

    images = [
        {"alt": m.group(1).strip(), "url": m.group(2).strip()}
        for m in IMAGE_RE.finditer(markdown_text)
    ]

    links = [
        {"text": m.group(1).strip(), "url": m.group(2).strip()}
        for m in LINK_RE.finditer(markdown_text)
    ]

    tables = _extract_pipe_tables(markdown_text)

    code_blocks = []
    for m in CODE_BLOCK_RE.finditer(markdown_text):
        language = m.group(1).strip()
        content = m.group(2).strip()
        code_blocks.append(
            {
                "language": language,
                "has_language_tag": str(bool(language)).lower(),
                "preview": content[:180],
            }
        )

    return ParsedMarkdown(
        headings=headings,
        images=images,
        links=links,
        tables=tables,
        code_blocks=code_blocks,
    )


def _extract_pipe_tables(markdown_text: str) -> List[str]:
    lines = markdown_text.splitlines()
    tables: List[str] = []
    i = 0
    while i < len(lines) - 1:
        line = lines[i]
        next_line = lines[i + 1]
        if "|" in line and _is_table_separator(next_line):
            buffer = [line, next_line]
            i += 2
            while i < len(lines) and "|" in lines[i].strip():
                buffer.append(lines[i])
                i += 1
            tables.append("\n".join(buffer))
        else:
            i += 1
    return tables


def _is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if "|" not in stripped:
        return False
    return bool(re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?", stripped))


def truncate_text(text: str, max_chars: int = 12000) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n[TRUNCATED FOR TOKEN LIMIT]"


def try_parse_json(content: str) -> Optional[dict]:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.replace("json", "", 1).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return None


def normalize_issue_ids(issues: List[dict]) -> List[dict]:
    seen = Counter()
    normalized = []
    for idx, issue in enumerate(issues, start=1):
        issue = dict(issue)
        issue_id = str(issue.get("id") or f"ISSUE-{idx}")
        seen[issue_id] += 1
        if seen[issue_id] > 1:
            issue_id = f"{issue_id}-{seen[issue_id]}"
        issue["id"] = issue_id
        normalized.append(issue)
    return normalized


def ensure_score_breakdown(payload: dict) -> dict:
    severity_penalties = {"high": 15, "medium": 8, "low": 3}
    issues = payload.get("issues", []) or []

    counts = Counter(issue.get("severity", "low") for issue in issues)
    penalties = []
    total_penalty = 0
    for sev in ("high", "medium", "low"):
        count = int(counts.get(sev, 0))
        per_item = severity_penalties[sev]
        subtotal = count * per_item
        penalties.append(
            {
                "severity": sev,
                "count": count,
                "penalty_per_item": per_item,
                "subtotal": subtotal,
            }
        )
        total_penalty += subtotal

    final_score = max(0, 100 - total_penalty)

    payload["score_breakdown"] = {
        "base": 100,
        "penalties": penalties,
        "final": final_score,
    }
    payload["score"] = final_score
    return payload
