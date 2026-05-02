"""AI scoring and proposal generation service."""

from __future__ import annotations

from app.db.models import AIRecommendation, Opportunity


class AIService:
    def score_opportunity(self, opportunity: Opportunity) -> AIRecommendation:
        score = 0.8 if opportunity.description else 0.4
        summary = f"Opportunity '{opportunity.title}' scored at {score:.2f}."
        return AIRecommendation(
            opportunity_id=opportunity.external_id,
            score=score,
            summary=summary,
        )

