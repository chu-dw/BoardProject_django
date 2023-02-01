from rest_framework import serializers

from users.serailizers import ProfileSerializer
from .models import Post

class PostSerializer(serializer.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image", "published_date", "likes")



class PostCreateSerializer(serializer.MoedeSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")
        