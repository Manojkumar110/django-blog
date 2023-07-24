from django import forms
from djangogirls.models import Post, User, Tags, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.db.models import fields  
from django.contrib.auth import get_user_model  
# from multivaluefield import MultiValueField

class PostForm(forms.ModelForm):
    # tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset = Tags.objects.all())
    # slug = forms.SlugField()
    class Meta:
        model = Post
        fields = ('title',  'text', 'image', 'feature_img', 'category', 'tags', 'created_date')

    
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ['user_profile', 'first_name', 'username','email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']

class LoginForm(forms.Form):
    # email = forms.EmailField()
    username = forms.CharField(label='Please Enter email or username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_profile', 'first_name', 'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')