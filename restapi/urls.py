from django.urls import path, include
from restapi import views


# urlpatterns = [
#     path('post/', views.PostList.as_view(), name='post'),
#     path('post/<int:pk>/', views.PostRetrieveUpdateDestroy.as_view(), name='post'),
# ]


urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name='post'),
    path('post/create/', views.PostCreateAPIView.as_view(), name='postcreate'),
    path('post/<int:pk>/', views.PostAPIView.as_view(), name='post'),
    path('category/', views.CategoryListApiView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryApiView.as_view(), name='category'),
    path('tags/', views.TagsListApiView.as_view(), name='tags'),
    path('tags/<int:pk>/', views.TagsApiView.as_view(), name='tags'),
    path('user/create/', views.UserListApiView.as_view(), name='usercraete'),
    path('user/create/<int:pk>/', views.UserApiView.as_view(), name='userdetail'),
    path('comment/', views.CommentListCreateApiView.as_view(), name='comment'),
    path('comment/<int:pk>/', views.CommentApiView.as_view(), name='commentdetail'),
]
