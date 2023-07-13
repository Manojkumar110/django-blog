from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title

