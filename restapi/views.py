# from djangogirls .models import Post, Category, Tags, User, Comment
# from restapi .serializers import PostSerializer, CategorySerializre, TagSerializer, UserSerializer, CommentSerializer
# from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
# from rest_framework.permissions import IsAuthenticated
# # Create your views here.


# class PostListAPIView(ListAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostCreateAPIView(CreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostAPIView(RetrieveUpdateDestroyAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class CategoryListApiView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializre


# class CategoryApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializre


# class TagsListApiView(ListCreateAPIView):
#     queryset = Tags.objects.all()
#     serializer_class = TagSerializer


# class TagsApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Tags.objects.all()
#     serializer_class = TagSerializer


# class UserListApiView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserApiView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class CommentListCreateApiView(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class CommentApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


from djangogirls .models import Post, Category, Tags, Comment, User
from restapi .serializers import PostSerializer, CategorySerializre, TagSerializer, UserSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.


class PostAPIView(viewsets.ModelViewSet):
    # permission_classes = ((AllowAny,))
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ["get", "put", "delete", "patch", "post"]


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


class CommentApiView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ["get", "put", "delete", "patch", "post"]
