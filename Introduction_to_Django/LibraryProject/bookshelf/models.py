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
    author= models.ForeignKey
    publication_date = models.DateField
class Meta:
    ordering = ['title', 'author', 'publication_date']
def __str__(self):
    return f"{self.title} by {self.author} published on {self.publication_date}"    
