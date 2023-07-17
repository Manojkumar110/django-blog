from django.urls import path
from djangogirls.views import post_list, author_detail, post_detail, post_new, post_edit, register, login_page, profile_view, profile_update, export
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('adnew/post/', post_new, name='post_new'),
    path('post/<str:slug>/edit/', post_edit, name='post_edit'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('profileview/', profile_view, name='userprofileview'),
    path('updateprofile/<int:pk>/edit', profile_update, name='updateprofile'),
    path('export/', export, name='userdataexport'),
    path('author/detail', author_detail, name='author_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


