"""Domain and persistence models."""

from __future__ import annotations

from dataclasses import dataclass

from django.db import models


class Opportunity(models.Model):
    external_id = models.CharField(max_length=255, unique=True)
    platform = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    budget = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.platform}: {self.title}"


@dataclass(slots=True)
class AIRecommendation:
    opportunity_id: str
    score: float
    summary: str


@dataclass(slots=True)
class BidRequest:
    opportunity: Opportunity
    proposal: str
