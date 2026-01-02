from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from base.serializers import CreatableSlugRelatedField
from messenger.models import Message, Tag

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
        read_only_fields = fields


class MessageSerializer(serializers.ModelSerializer):
    tags = CreatableSlugRelatedField(
        slug_field="name",
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Message
        fields = (
            "id",
            "created_at",
            "user",
            "text",
            "text_preview",
            "tags"
        )
        extra_kwargs = {"text": {"write_only": True}}


class MessageDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ("id", "created_at", "text", "user")
