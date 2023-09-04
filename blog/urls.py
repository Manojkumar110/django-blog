from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangogirls.urls')),
    path('polls/', include('djangopolls.urls')),
    path('api/v1/', include('restapi.urls')),
]

admin.site.site_header = 'BLOG ADMIN'
admin.site.index_title = "Welcome to Blog Portal"
