from rest_framework import serializers
from django.conf import settings
from .models import Notion

MAX_NOTION_LENGTH = settings.MAX_NOTION_LENGTH
NOTION_ACTION_OPTION = settings.NOTION_ACTION_OPTION


class NotionActionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in NOTION_ACTION_OPTION:
            raise serializers.ValidationError(
                "This is not a valid action for notions")
        return value


class NotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notion
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_NOTION_LENGTH:
            raise serializers.ValidationError("This notion is too long")
        return value
