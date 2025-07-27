from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField
    #... additional fields and methods as required ...

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Email Must Be Set'))
        email = self.mormalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra.fields.setdefault('is_admin', True)
        extra.fields.setdefault('is_librarian', True)
        extra.fields.setdefault('is_member', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError(_('Superuser must have is_admin=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))



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

