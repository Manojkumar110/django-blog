from rest_framework import serializers
from djangogirls .models import Post, Category, Tags, User, Comment
from django.contrib.auth import authenticate


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "author", "title", "text", "image",
                  "feature_img", "category", "tags"]


class CategorySerializre(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "image", "description", "slug"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ["id", "name", "image", "description", "slug"]


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


# User = get_user_model()
# class LoginSerializers(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(
#         label=_("Password"),
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         max_length=128,
#         write_only=True
#     )

#     def validate(self, data):
#         username = data.get('email')
#         password = data.get('password')

#         if username and password:
#             user = authenticate(request=self.context.get('request'),
#                                 username=username, password=password)
#             if not user:
#                 msg = _('Unable to log in with provided credentials.')
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = _('Must include "username" and "password".')
#             raise serializers.ValidationError(msg, code='authorization')
#         data['user'] = user
#         return data
