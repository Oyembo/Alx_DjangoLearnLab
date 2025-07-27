from bookshelf.models import Author, Book
author_orwell = Author.objects.create(
    first_name = "George"
    last_name = "Orwell"
)
def __str__(self):
    return f"{self.first_name}, {self.last_name}
    return George Orwell
book_1984 = Book.objects.create(
    title = "1984"
    author = author-orwell
    publication_date = "1949"
)