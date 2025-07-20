from django.contrib import admin
from .models import Book, Author

# Register your models here using the @admin.register decorator.
# The explicit admin.site.register() calls are removed as they are redundant
# when using the decorator, and cause the AlreadyRegistered error.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('last_name', 'first_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    # Corrected the unterminated string literal by adding the closing quote and parenthesis
    search_fields = ('author', 'publication_year',)