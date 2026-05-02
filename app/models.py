"""Bridge module so Django can discover models in app.db.models."""

from app.db.models import AIRecommendation, BidRequest, Opportunity

__all__ = ["AIRecommendation", "BidRequest", "Opportunity"]

