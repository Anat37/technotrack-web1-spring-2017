# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)


class UserAdmin(BaseUserAdmin):

    fieldsets = BaseUserAdmin.fieldsets

    def admin_avatar(self, instance):
        return instance.avatar and u'<img src="{0}" width="100px" />'.format(
            instance.avatar.url
        )
    admin_avatar.allow_tags = True
    admin_avatar.short_description = u'Аватар'
