from django.db import models

# Create your models here.
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    def Book (self):
        print(f"This Book {self.title} by {self.author} was published in {self.publication_year}")
