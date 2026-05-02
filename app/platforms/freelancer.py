"""Freelancer platform client."""

from __future__ import annotations

from typing import Any


class FreelancerPlatformClient:
    platform_name = "freelancer"

    def fetch_jobs(self) -> list[dict[str, Any]]:
        """Fetch raw jobs from the Freelancer source."""
        return []

