"""API-based ingestion strategy."""

from __future__ import annotations

from typing import Any, Protocol


class APIClient(Protocol):
    def fetch_jobs(self) -> list[dict[str, Any]]:
        ...


class APIStrategy:
    def fetch(self, client: APIClient) -> list[dict[str, Any]]:
        return client.fetch_jobs()

