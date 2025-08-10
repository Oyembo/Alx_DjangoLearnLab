from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book, with a foreign key to Author.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title