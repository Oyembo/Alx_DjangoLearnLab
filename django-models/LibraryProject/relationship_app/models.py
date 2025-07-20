from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class Meta:
        ordering = ['first_name', 'last_name']
    def __str__(self):
        return f'{self.first_name}, '{self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManytoManyField(Book,related_name= 'Library')

class Librarian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    library = models.OneToOneField(Library)
    class Meta:
        ordering = ['first_name', 'last_name', 'library']
    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.library}'

