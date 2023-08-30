from rest_framework import serializers
from djangogirls .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title", "text", "image", "feature_img", "category", "tags"]