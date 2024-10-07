# yatube_api/api/serializers.py

from rest_framework import serializers

from posts.models import Comment, Group, Post, Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['user', 'following']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'pub_date', 'image', 'group')

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
