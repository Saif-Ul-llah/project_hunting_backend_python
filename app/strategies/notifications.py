"""Notification strategy."""

from __future__ import annotations

from app.db.models import Opportunity


class NotificationStrategy:
    def build_message(self, opportunity: Opportunity) -> str:
        return f"[{opportunity.platform}] {opportunity.title}"

    def send(self, message: str) -> bool:
        return bool(message)

