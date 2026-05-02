"""Worker that runs ingestion tasks."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from app.services.ingestion_service import IngestionService


class IngestionWorker:
    def __init__(self, service: IngestionService) -> None:
        self.service = service

    def run_once(
        self,
        raw_jobs: list[dict[str, Any]],
        adapter: Callable[[dict[str, Any]], Any],
    ) -> int:
        return len(self.service.ingest(raw_jobs, adapter))

