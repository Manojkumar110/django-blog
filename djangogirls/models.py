from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse
from django.utils.text import slugify

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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to = 'postimg/', null=True, blank=True)
    feature_img = models.ImageField(upload_to = 'featureimg/', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tags, related_name='post_tag')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now_add = True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)