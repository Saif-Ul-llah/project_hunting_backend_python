"""Bid evaluation and generation service."""

from __future__ import annotations

from app.db.models import BidRequest, Opportunity
from app.services.ai_service import AIService


class BiddingService:
    def __init__(self, ai_service: AIService) -> None:
        self.ai_service = ai_service

    def build_bid_request(self, opportunity: Opportunity) -> BidRequest:
        recommendation = self.ai_service.score_opportunity(opportunity)
        proposal = (
            f"Proposal for {opportunity.title}: "
            f"recommended score {recommendation.score:.2f}."
        )
        return BidRequest(opportunity=opportunity, proposal=proposal)

