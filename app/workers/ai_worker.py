"""Worker that runs AI analysis tasks."""

from __future__ import annotations

from app.db.models import Opportunity
from app.services.ai_service import AIService


class AIWorker:
    def __init__(self, service: AIService) -> None:
        self.service = service

    def run_once(self, opportunity: Opportunity) -> float:
        recommendation = self.service.score_opportunity(opportunity)
        return recommendation.score

