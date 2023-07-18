from django import forms
from djangogirls.models import Post, User, Comment, Tags
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.db.models import fields  
from django.contrib.auth import get_user_model  
    


# class DateInput(forms.DateInput):
#     input_type = 'date'

class PostForm(forms.ModelForm):
#     tags = forms.ModelMultipleChoiceField(queryset=Post.tags.all(),
#     widget=forms.CheckboxSelectMultiple
#   )
    class Meta:
        model = Post
        fields = ('title', 'slug', 'text', 'image', 'feature_img', 'category', 'tags', 'created_date')
        # exclude = ['author']
        # widgets = {
        #     'dob': DateInput()
        # }
    
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
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