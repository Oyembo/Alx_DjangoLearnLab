from django.contrib import admin
from .models import Book, Author, Library, Librarian

# Register your models here using the @admin.register decorator.
# The explicit admin.site.register() calls are removed as they are redundant
# when using the decorator, and cause the AlreadyRegistered error.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('last_name', 'first_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_date') 
    search_fields = ('author', 'publication_date')

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name' ,)
    search_fields = ('name' ,) #Search library by name
    filter_horizontal = ('books' ,)

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library__name')
