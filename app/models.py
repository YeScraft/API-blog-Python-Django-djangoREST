from django.db import models
from django.db.models import SET_NULL
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('category', on_delete=SET_NULL, blank=True, null=True, related_name='posts')
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, related_name='author')


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField

    def __str__(self):
        return self.title
