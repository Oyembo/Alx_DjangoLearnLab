from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('title', 'author') # Search book by author and book title

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'books')
    list_filter = ('books') #Search books in library

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library')
