from blogs.models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        """fileds = [
            # "created_at",
            "image",
            "title",
            "author",
            "category",
            "tags",
            "short_description",
            "description",
        ]"""
        exclude = ["created_at"]
