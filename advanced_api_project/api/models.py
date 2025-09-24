from django.db import models

class Author(models.Model):
    """
    A data model that defines authors
    """
    name = models.CharField(max_length=100)


class Book(models.Model):
    """
    Book data model. Defines books woth one-to-many relationship witht the author
    """
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
