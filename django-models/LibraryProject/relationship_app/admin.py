from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name' ,)
    search_fields = ('name' ,)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('title', 'author__name', 'publication_date') # Search book by author and book title

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name' ,)
    search_fields = ('name' ,)
    filter_horizontal = ('books' ,) #Search books in library

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library__name')
