from django.contrib import admin
from .models import Book, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter =('last_name', 'first_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author','publication_year')
    search_fields = ('author', 'publication_year')