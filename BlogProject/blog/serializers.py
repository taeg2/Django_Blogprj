from rest_framework import serializers
from .models import Posting, Reples

class RepleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reples
        fields = ["id", "comments", "date"]

class PostSerializer(serializers.ModelSerializer):
    reples = RepleSerializer(many=True, read_only=True)

    class Meta:
        model = Posting
        fields = ["id", "title", "description", "date", "reples"]