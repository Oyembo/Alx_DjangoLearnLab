import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models impory Author, Book, Library, Librarian

def run_queries():
    print("---Initializing and Running Queries---")

    print("Creating sample data...")

    author1, created = Author.objects.get_or_create(name="Kithaka Wamberia")
    if created: print(f"Created Author: {author1.name}")
    author2, created = Author.objects.get_or_create(name="Margaret Ogot")
    if created: print(f"Created Author: {author2.name}")
    author3, created = Author.objects.get_or_create(name="Ngugi Wa Thiong'o")
    if created: print(f"Created Author: {author3.name}")

    book1, created = Book.objects.get_or_create(title="Kifo Kisimani", author=author1)
    if created: print(f"Created Book: {book1.title}")
    book2, created = Book.objects.get_or_create(title="The River and the Source", author=author2)
    if created: print(f"Created Book: {book2.title}")
    book3, created = Book.objects.get_or_create(title="The River Between", author=author2)
    if created: print(f"Created Book: {book3.title}")
    book4, created = Book.objects.get_or_create(title="Weep O Child", author=author3)
    if created: print(f"Created Book: {book4.title}")

    library1, created = Library.objects.get_or_create(name="MacMillan Library")
    if created: print(f"Created Library: {library1.name}")
    library2, created = Library.objects.get_or_create(name="Upperhill KNLS Library")
    if created: print(f"Created Library: {library2.name}")

    library1.books.set([book1, book2])
    print(f"Added books to {library1.name}")
    library2.books.set([book2, book3, book4])
    print(f"Added books to {library2.name}")

    librarian1, created = Librarian.objects.get_or_create(name="Wanjiku Acholla", library=library1)
    if created: print(f"Created Librarian: {librarian1.name}")
    librarian2, created = Librarian.objects.get_or_create(name="Kemunta Nekesa", library=library2)
    if created: print(f"Created Librarian: {librarian2.name}")

    print("\n--- Query Results ---")

    print("\n1. All books by Kithaka Wamberia:")
    kithaka_wamberia_books = Book.objects.filter(author__name="Kithaka Wamberia)
    for book in kithaka_wamberia_books:
        print(f"  - {book.title}")

    print("\n2. All books in Upperhill KNLS Library:")
    upperhill_knls_library = Library.objects.get(name="Upperhill KNLS Library")
    for book in upperhill_knls_library.books.all():
        print(f"  - {book.title}")

    print("\n3. Librarian for MacMillan Library:")
    macmillan_library = Library.objects.get(name="MacMillan Library")
    try:
        librarian = macmillan_library.librarian_in_charge
        print(f"  - {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"  - No librarian found for {macmillan_library.name}")

    print("\n--- Queries Complete ---")

if __name__ == '__main__':
    run_queries()
