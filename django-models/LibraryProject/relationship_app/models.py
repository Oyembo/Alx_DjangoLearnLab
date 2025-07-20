from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    LIBRARIAN = 'librarian', 'Librarian'
    MEMBER = 'member', 'Member'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50
    choices = UserRole.choices
    default = UserRole.MEMBER
    )

class Author(models.Model):
    name = models.CharField(max_length=100)   

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books_by_author')
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book,related_name= 'library_containing')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name = 'librarian_in_charge')

    class Meta:
        ordering = ['name', 'library']
    def __str__(self):
        return f'{self.name}, {self.library}'

