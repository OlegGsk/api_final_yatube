# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from posts.models import Comment, Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    pagination_class = (LimitOffsetPagination,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)