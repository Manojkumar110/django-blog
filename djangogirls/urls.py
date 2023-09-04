from django.urls import path
from djangogirls.views import post_list, user_logout,\
 author_detail, post_detail, post_new, post_edit, register,\
login_page, profile_view, profile_update, postCategory, catDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('adnew/post/', post_new, name='post_new'),
    path('post/<str:slug>/edit/', post_edit, name='post_edit'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('user/logout/', user_logout, name='userlogout'),
    path('profileview', profile_view, name='userprofileview'),
    path('updateprofile/<int:pk>/edit', profile_update, name='updateprofile'),
    path('authordetail/', author_detail, name='author_detail'),
    path('post/category', postCategory, name='post_category'),
    path('category/detail/<int:pk>/', catDetail, name='cat_detail')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


