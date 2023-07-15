from django.urls import path
from djangogirls.views import post_list, post_detail, post_new, post_edit, register, login_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('adnew/post/', post_new, name='post_new'),
    path('post/<str:slug>/edit/', post_edit, name='post_edit'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


