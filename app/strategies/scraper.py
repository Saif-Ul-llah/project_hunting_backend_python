"""Scraper-based ingestion strategy."""

from __future__ import annotations

from typing import Any, Protocol


class ScraperClient(Protocol):
    def scrape_jobs(self) -> list[dict[str, Any]]:
        ...


class ScraperStrategy:
    def fetch(self, client: ScraperClient) -> list[dict[str, Any]]:
        return client.scrape_jobs()

