"""Django admin registrations."""

from django.contrib import admin

from app.db.models import Opportunity


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("external_id", "platform", "title", "processed", "created_at")
    list_filter = ("platform", "processed", "created_at")
    search_fields = ("external_id", "title", "description")

