from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
class Book(models.Model):
    title = models.CharField (max_length=200)
    author= models.ForeignKey(Author, on_delete=models.CASCADE, related_name= 'books_written')
    publication_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['title', 'author', 'publication_date']

    def __str__(self):
        return f"{self.title} by {self.author} published on {self.publication_date}"   

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book,related_name= 'libraries_holding')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name = 'librarian_in_charge')
    
    class Meta:
        ordering = ['name', 'library']
    def __str__(self):
        return f'{self.name}, {self.library}'

