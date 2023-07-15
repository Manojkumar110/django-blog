from django import forms
from djangogirls.models import Post, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.db.models import fields  
from django.contrib.auth import get_user_model  
    


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
    
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        exclude = ['password', 'last_login', ]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
