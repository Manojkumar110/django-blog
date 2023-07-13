from django.urls import path
from djangogirls.views import post_list, post_detail, post_new, post_edit

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('adnew/post/', post_new, name='post_new'),
    path('post/<str:slug>/edit/', post_edit, name='post_edit'),
]


