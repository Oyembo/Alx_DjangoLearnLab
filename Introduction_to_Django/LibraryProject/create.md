from bookshelf.models import Author, Book
author_orwell = Author.objects.create(
    first_name = "George"
    last_name = "Orwell"
)
book_1984 = Book.objects.create(
    title = "1984"
    author = author-orwell
    publication_date = "1949"
)