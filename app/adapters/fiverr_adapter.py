"""Fiverr payload adapter."""

from __future__ import annotations

from typing import Any

from app.db.models import Opportunity


def adapt_fiverr_job(payload: dict[str, Any]) -> Opportunity:
    return Opportunity(
        external_id=str(payload.get("id", "")),
        platform="fiverr",
        title=payload.get("title", "Untitled Fiverr Job"),
        description=payload.get("description", ""),
        budget=str(payload.get("budget", "")) or None,
        url=payload.get("url", ""),
        metadata=payload,
    )

