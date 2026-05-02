"""Django REST Framework route and view definitions."""

from __future__ import annotations

from django.urls import path
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.serializers import BidEvaluationInputSerializer
from app.db.models import Opportunity
from app.db.repository import DjangoOpportunityRepository
from app.services.ai_service import AIService
from app.services.bidding_service import BiddingService
from app.services.ingestion_service import IngestionService

repository = DjangoOpportunityRepository()
ingestion_service = IngestionService(repository=repository)
bidding_service = BiddingService(ai_service=AIService())


class HealthcheckView(APIView):
    authentication_classes: list[type] = []
    permission_classes: list[type] = []

    def get(self, request: Request) -> Response:
        return Response({"status": "ok"})


class TriggerIngestionView(APIView):
    def post(self, request: Request) -> Response:
        return Response(
            {
                "message": "Ingestion endpoint initialized",
                "service": ingestion_service.__class__.__name__,
            }
        )


class EvaluateBidView(APIView):
    def post(self, request: Request) -> Response:
        serializer = BidEvaluationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payload = serializer.validated_data

        opportunity = Opportunity(
            external_id=payload.get("external_id", "preview-opportunity"),
            platform=payload.get("platform", "manual"),
            title=payload.get("title", "Untitled Opportunity"),
            description=payload.get("description", ""),
            budget=payload.get("budget"),
            url=payload.get("url", ""),
            metadata=payload.get("metadata", {}),
        )
        bid_request = bidding_service.build_bid_request(opportunity)
        return Response({"proposal": bid_request.proposal}, status=status.HTTP_200_OK)


urlpatterns = [
    path("health/", HealthcheckView.as_view(), name="healthcheck"),
    path("ingest/", TriggerIngestionView.as_view(), name="trigger-ingestion"),
    path("bids/evaluate/", EvaluateBidView.as_view(), name="evaluate-bid"),
]
