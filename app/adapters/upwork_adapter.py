"""Upwork payload adapter."""

from __future__ import annotations

from typing import Any

from app.db.models import Opportunity


def adapt_upwork_job(payload: dict[str, Any]) -> Opportunity:
    return Opportunity(
        external_id=str(payload.get("id", "")),
        platform="upwork",
        title=payload.get("title", "Untitled Upwork Job"),
        description=payload.get("description", ""),
        budget=str(payload.get("budget", "")) or None,
        url=payload.get("url", ""),
        metadata=payload,
    )

