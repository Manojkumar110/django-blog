from djangogirls .models import Post, Category, Tags, User, Comment
from restapi .serializers import PostSerializer, CategorySerializre, TagSerializer, UserSerializer, CommentSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostListAPIView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializre

class CategoryApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializre

class TagsListApiView(ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TagsApiView(RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class UserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentListCreateApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentApiView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
