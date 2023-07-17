from django import forms
from djangogirls.models import Post, User, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.db.models import fields  
from django.contrib.auth import get_user_model  
    


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
    
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # exclude = ['password', 'last_login', 'superuser_status']
        fields = ['user_profile', 'first_name', 'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_profile', 'first_name', 'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')