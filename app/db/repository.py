"""Repository abstractions and Django ORM implementation."""

from __future__ import annotations

from typing import Protocol

from app.db.models import Opportunity


class OpportunityRepository(Protocol):
    def save(self, opportunity: Opportunity) -> Opportunity:
        ...

    def list_all(self) -> list[Opportunity]:
        ...


class DjangoOpportunityRepository:
    def save(self, opportunity: Opportunity) -> Opportunity:
        defaults = {
            "platform": opportunity.platform,
            "title": opportunity.title,
            "description": opportunity.description,
            "budget": opportunity.budget,
            "url": opportunity.url,
            "metadata": opportunity.metadata,
            "processed": opportunity.processed,
        }
        stored, _ = Opportunity.objects.update_or_create(
            external_id=opportunity.external_id,
            defaults=defaults,
        )
        return stored

    def list_all(self) -> list[Opportunity]:
        return list(Opportunity.objects.all())
