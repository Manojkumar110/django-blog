from djangogirls .models import Post, Category, Tags, Comment, User
from restapi .serializers import PostSerializer, CategorySerializre, TagSerializer, UserSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ["get", "put", "delete", "patch", "post"]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title',]
    search_fields = ['title',]


class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializre
    http_method_names = ["get", "put", "delete", "patch", "post"]


class TagsApiView(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    http_method_names = ["get", "put", "delete", "patch", "post"]


class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "put", "delete", "patch", "post"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'email', 'city', 'phone_no']


class CommentApiView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ["get", "put", "delete", "patch", "post"]
