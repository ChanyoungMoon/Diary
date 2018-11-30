from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'

    class Meta:
        ordering = ['-pk']
