from rest_framework.serializers import ModelSerializer
from .models import Post
from django.contrib.auth import get_user_model


class PostSerializer(ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")
