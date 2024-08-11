from django.db import models
from authors.models import Author


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=35, unique=True)
    fk_book_to_author = models.ForeignKey(Author, default=0, on_delete=models.CASCADE)
