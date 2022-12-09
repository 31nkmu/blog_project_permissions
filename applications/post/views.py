from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework import permissions

from applications.post.models import Post, Category, Comment
from applications.post.permissions import IsOwner, IsCommentOwner
from applications.post.serializers import PostSerializer, CategorySerializer, CommentSerializer


# class PostApiView(ViewSet):
#     @staticmethod
#     def list(request):
#         post = Post.objects.all()
#         serializer = PostSerializer(post, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @staticmethod
#     def create(request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostApiView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'owner']
    search_fields = ['title', 'description']

    # ordering_fields = ['id']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     category = self.request.query_params.get('category')
    #     if category:
    #         queryset = queryset.filter(category=category)
    #         return queryset
    #     return None


class CategoryApiView(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentApiView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        owner = self.request.user.id
        queryset = super().get_queryset()
        res = queryset.filter(owner=owner)
        return res
