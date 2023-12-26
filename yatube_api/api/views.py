# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post, Follow
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .mixins import ListCreateViewSet
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = LimitOffsetPagination
    lookup_url_kwarg = 'id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_object(self):
        get_object_or_404(Post, pk=self.kwargs.get('id'))
        return super().get_object()


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=self.get_post())

    def get_queryset(self):
        comments = self.get_post().comments.all()
        return comments

    def get_object(self):
        get_object_or_404(Comment, pk=self.kwargs.get('id'),
                          post_id=self.kwargs.get('post_id'))
        return super().get_object()

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class FollowViewSet(ListCreateViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
