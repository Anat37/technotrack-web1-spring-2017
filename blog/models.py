from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):

    title = models.CharField(max_length=255)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
