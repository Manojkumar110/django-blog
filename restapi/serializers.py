from rest_framework import serializers
from djangogirls .models import Post, Category, Tags, User, Comment
# from django.contrib.auth import authenticate


class CategorySerializre(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = ["id", "name", "image", "description", "slug"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ["id", "name", "image", "description", "slug"]


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializre(many=False)
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = ["id", "author", "title", "text", "image",
                  "feature_img", "category", "tags"]

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True, max_length=255, allow_blank=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'username', 'email', 'user_profile', 'city',
                  'gender', 'state', 'dob', 'country', 'zip_code', 'phone_no', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'body', 'active', 'post', 'parent']


