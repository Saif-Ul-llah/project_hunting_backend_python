"""Application configuration primitives."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(slots=True)
class Settings:
    app_name: str = "freelance-backend"
    environment: str = os.getenv("APP_ENV", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    polling_interval_seconds: int = int(os.getenv("POLLING_INTERVAL_SECONDS", "60"))
    notification_webhook: str | None = os.getenv("NOTIFICATION_WEBHOOK")


def get_settings() -> Settings:
    """Return application settings loaded from environment variables."""
    return Settings()

