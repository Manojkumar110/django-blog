from django.contrib import admin
from djangogirls.models import Post, Category, Tags

# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}


class TagsModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

class PostModelAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'slug', 'text', 'category', 'tags', 'created_date',]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Tags, TagsModelAdmin)