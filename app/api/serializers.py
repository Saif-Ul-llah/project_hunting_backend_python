"""API serializers."""

from rest_framework import serializers


class BidEvaluationInputSerializer(serializers.Serializer):
    external_id = serializers.CharField(required=False, default="preview-opportunity")
    platform = serializers.CharField(required=False, default="manual")
    title = serializers.CharField(required=False, default="Untitled Opportunity")
    description = serializers.CharField(required=False, default="", allow_blank=True)
    budget = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    url = serializers.URLField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False, default=dict)
