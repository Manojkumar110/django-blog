from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from djangogirls.models import Post, Category, Tags, User, Comment
from django.utils.html import format_html

# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_filter = ['name']


class TagsModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_filter = ['name']


class PostModelAdmin(admin.ModelAdmin):

    def post_image(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    
    fields = ['author', 'image','title', 'slug', 'text', 'category', 'tags', 'created_date',]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['author', 'title', 'category', 'tags', 'published_date']
    list_display = ['author',  'post_image', 'post_title', 'category', 'published_date']

    def post_title(self, obj):
        return format_html(f"<a href='/post/{obj.slug}'>{obj.title}</h1>")


class UserModelAdmin(admin.ModelAdmin):
    def profile(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.user_profile.url))

    list_display = ['first_name', 'profile', 'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']

    

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'post_title', 'body', 'created_on', 'active']

    def post_title(self, obj):
        return format_html(f"<p>{obj.post.title}</p>")

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Tags, TagsModelAdmin)
admin.site.register(User, UserModelAdmin)
admin.site.register(Comment, CommentModelAdmin)

