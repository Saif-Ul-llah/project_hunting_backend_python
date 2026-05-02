"""Fiverr platform client."""

from __future__ import annotations

from typing import Any


class FiverrPlatformClient:
    platform_name = "fiverr"

    def fetch_jobs(self) -> list[dict[str, Any]]:
        """Fetch raw jobs from the Fiverr source."""
        return []

