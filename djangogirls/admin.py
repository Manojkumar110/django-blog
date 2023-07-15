from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from djangogirls.models import Post, Category, Tags, User

# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}


class TagsModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    

class PostModelAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'slug', 'text', 'category', 'tags', 'created_date',]
    prepopulated_fields = {"slug": ("title",)}

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'user_profile',]

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Tags, TagsModelAdmin)
admin.site.register(User, UserModelAdmin)

