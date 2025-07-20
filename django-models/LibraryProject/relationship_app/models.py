from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)     
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManytoManyField(Book,related_name= 'Library')

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library)
    class Meta:
        ordering = ['name', 'library']
    def __str__(self):
        return f'{self.name}, {self.library}'

