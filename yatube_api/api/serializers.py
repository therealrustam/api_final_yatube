from posts.models import Comment, Follow, Group, Post
from rest_framework import serializers
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
    user = serializers.SlugRelatedField(
        read_only=True, required=False, slug_field='username')
    following = FollowingSerializer()

    class Meta:
        model = Follow
        fields = ('user', 'following',)

    def create(self, validated_data):
        following = validated_data.get('following')
        validated_data.pop('following')
        follow = Follow.objects.create(following=following,
                                       **validated_data)
        return follow


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
