from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from djangogirls.models import Post, Category, Tags, User, Comment
from django.utils.html import format_html
from import_export.admin import ExportActionMixin
# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ['name', 'slug', 'image', 'description']
    list_filter = ['name']
    search_fields = ['name']


class TagsModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ['name', 'slug', 'image', 'description']
    list_filter = ['name']
    search_fields = ['name']


class PostModelAdmin(admin.ModelAdmin):
    # change_form_template = 'admin/change_form_object_tools.html'
    def post_title(self, obj):
        return format_html(f"<a href='/post/{obj.slug}'>{obj.title}</a>")

    def post_image(self, obj):
        if obj.feature_img:
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.feature_img.url))
        else:
            return ''
    fields = ['author', 'image',  'feature_img', 'title', 'slug', 'text', 'category', 'tags', 'created_date',]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['author', 'title', 'category', 'tags', 'published_date']
    list_display = ['author',  'post_image', 'post_title', 'category', 'published_date']
    search_fields = ['title', 'category', 'tags']
    view_on_site = True


class UserModelAdmin(ExportActionMixin, admin.ModelAdmin):
    def profile(self, obj):
        if obj.user_profile:
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.user_profile.url))
        else:
            return ''
    list_display = ['first_name', 'username', 'profile', 'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']
    list_filter = ['first_name',  'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']
    search_fields = ['first_name',  'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post_title',]
    list_filter = ['name']
    search_fields = ['name']

    def post_title(self, obj):
        return format_html(f"<p>{obj.post.title}</p>")

    def user_name(self, obj):
        return format_html(f"<p>{obj.user.first_name}</p>")

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Tags, TagsModelAdmin)
admin.site.register(User, UserModelAdmin)
admin.site.register(Comment, CommentModelAdmin)


