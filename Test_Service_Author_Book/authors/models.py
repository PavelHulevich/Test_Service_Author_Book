from django.db import models


class Author(models.Model):
    objects = None
    name = models.CharField(max_length=35, unique=True)
