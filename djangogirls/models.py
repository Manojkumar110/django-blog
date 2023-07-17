from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 
from django.utils.html import mark_safe



# # Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'catimg/', blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'tagimg/', blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to = 'postimg/', blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tags)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now_add = True)



class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    STATE_CHOICES = (
        ("rajasthan", "rajasthan"),
        ("punjab", "punjab"),
        ("uttarpradesh", "uttarpradesh"),  
    )
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(_('email address'), unique = True)
    user_profile = models.ImageField(upload_to='avatar', blank=True, null=True)
    city = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices = GENDER_CHOICES, default='')
    state = models.CharField(max_length=200, choices = STATE_CHOICES, default='')
    dob = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=200)
    zip_code = models.IntegerField(null = True)
    phone_no = models.CharField(max_length = 10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return "{}".format(self.email)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['created_on']

    # def __str__(self):
    #     return f"{self.}"


# class ReplyComment(models.Model):
#    reply_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
#    replier_name = models.CharField(max_length=200)
#    reply_content = models.TextField()
#    replied_date = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return self.replier_name
