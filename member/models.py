from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.db.models import Q


class UserManager(BaseUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(*args, **kwargs)


class User(AbstractUser):

    objects = UserManager()

    def __str__(self):
        return self.username

