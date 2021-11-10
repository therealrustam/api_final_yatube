from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowingSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        return value.username


class FollowSerializer(serializers.ModelSerializer):
   # user = serializers.SlugRelatedField(
    #    read_only=True, required=False, slug_field='username')
    user = FollowingSerializer(required=False)
    following = FollowingSerializer(required=True)

    class Meta:
        model = Follow
        fields = ('user', 'following',)

    def create(self, validated_data):
        following = validated_data.pop('following')
        following = get_object_or_404(User, username=following)
        follow = Follow.objects.create(
            following=following, user=self.request.user, **validated_data)
        follow.save()
        return follow


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
