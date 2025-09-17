from rest_framework import serializers

from blog.models import Posting, Reples

class ReplesSerailzer(serializers.ModelSerializer):
    class Meta:
        model = Reples
        fields = "__all__"

class PostingSerializer(serializers.ModelSerializer):
    reples = ReplesSerailzer(many = True, read_only = True)

    class Meta:
        model = Posting
        fields = ["id", "title", "description", "date", "reples"]