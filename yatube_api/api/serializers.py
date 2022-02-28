"""
Параметры сериализаторов для моделей.
"""
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели постов.
    """
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели сообщества.
    """

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели подписок.
    """
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())

    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following']), ]

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписываться на себя!'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели комментариев.
    """
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
