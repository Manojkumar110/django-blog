from django.urls import path, include
from restapi import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', views.PostAPIView, basename='post'),
router.register('category', views.CategoryApiView, basename='category'),
router.register('tags', views.TagsApiView, basename='tags'),
router.register('user', views.UserApiView, basename='user'),
router.register('comment', views.CommentApiView, basename='comment'),


urlpatterns = [
    path('', include(router.urls)),
]
