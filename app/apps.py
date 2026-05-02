"""Django application configuration."""

from django.apps import AppConfig


class AppConfigBase(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
    verbose_name = "Freelance Automation Backend"

