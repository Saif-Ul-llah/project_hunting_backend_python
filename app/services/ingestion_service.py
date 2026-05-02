"""Ingestion orchestration service."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from app.db.models import Opportunity
from app.db.repository import OpportunityRepository

Adapter = Callable[[dict[str, Any]], Opportunity]


class IngestionService:
    def __init__(self, repository: OpportunityRepository) -> None:
        self.repository = repository

    def ingest(self, raw_jobs: list[dict[str, Any]], adapter: Adapter) -> list[Opportunity]:
        opportunities = [adapter(job) for job in raw_jobs]
        for opportunity in opportunities:
            self.repository.save(opportunity)
        return opportunities

