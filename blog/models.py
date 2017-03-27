from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=255)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('blog.Category', related_name='blogs')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey('blog.Blog', related_name='posts')

    def __str__(self):
        return self.title


class Attach(models.Model):
    attached_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('blog.Post', related_name='attaches')


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes')
    post = models.ForeignKey('blog.Post', related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
