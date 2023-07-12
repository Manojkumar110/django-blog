from django.contrib import admin
from djangogirls.models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'slug', 'text', 'created_date',]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostModelAdmin)