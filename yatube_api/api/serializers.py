from django.contrib.auth import get_user_model
from posts.models import Comment, Follow, Group, Post
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from .extra_fields_serializers import Base64ImageField

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        image = Base64ImageField(required=False, allow_null=True)
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post', 'created')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True,
                            default=serializers.CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('user', 'following')

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны!'
            )
        ]

    def validate(self, data):
        if data['following'] == self.context["request"].user:
            raise serializers.ValidationError(
                'Вы не можете подписаться на самого себя!')
        return data
