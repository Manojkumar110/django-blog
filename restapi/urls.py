from django.urls import path, include
from restapi import views


urlpatterns = [
    path('post/', views.PostList.as_view(), name='post'),
    path('post/<int:pk>/', views.PostRetrieveUpdateDestroy.as_view(), name='post'),
]