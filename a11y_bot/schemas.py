from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, Field, model_validator


Severity = Literal["low", "medium", "high"]


class PenaltyItem(BaseModel):
    severity: Severity
    count: int = Field(ge=0)
    penalty_per_item: int = Field(ge=0)
    subtotal: int = Field(ge=0)


class ScoreBreakdown(BaseModel):
    base: int = Field(ge=0, le=100)
    penalties: List[PenaltyItem]
    final: int = Field(ge=0, le=100)


class AccessibilityIssue(BaseModel):
    id: str = Field(min_length=1)
    severity: Severity
    title: str = Field(min_length=1)
    explanation: str = Field(min_length=1)
    evidence: str = Field(min_length=1)
    suggestion: str = Field(min_length=1)


class AccessibilityReviewResponse(BaseModel):
    score: int = Field(ge=0, le=100)
    score_breakdown: ScoreBreakdown
    summary_bullets: List[str] = Field(default_factory=list)
    issues: List[AccessibilityIssue] = Field(default_factory=list)
    applied_rules: Optional[str] = None

    @model_validator(mode="after")
    def validate_scores(self) -> "AccessibilityReviewResponse":
        if self.score_breakdown.base != 100:
            raise ValueError("score_breakdown.base must be 100")
        if self.score != self.score_breakdown.final:
            raise ValueError("score must equal score_breakdown.final")
        if len(self.summary_bullets) < 3:
            raise ValueError("summary_bullets must contain at least 3 items")
        if len(self.summary_bullets) > 6:
            raise ValueError("summary_bullets must contain at most 6 items")
        return self
