"""Upwork platform client."""

from __future__ import annotations

from typing import Any


class UpworkPlatformClient:
    platform_name = "upwork"

    def fetch_jobs(self) -> list[dict[str, Any]]:
        """Fetch raw jobs from the Upwork source."""
        return []

