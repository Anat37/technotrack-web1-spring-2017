from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Post(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey('blog.Blog', related_name='posts')

class Attach(models.Model):
    image = models.ImageField()
    attached_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('post.Post', related_name='attaches')

