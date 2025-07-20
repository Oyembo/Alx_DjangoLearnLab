from django.shortcuts import render
from .models import Library
from models import Book

# Create your views here.
def book_list(request):
    """Retrieves all books and renders a template displaying the list"""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, relationship_app/list_books.html)

class LibraryDetailView(DetailView):
    """A class-based view for displaying details of specific Library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book"""
        context = super().get_context_data(**kwargs) #Get default context data
        library = Library.objects.get(name=library__name) #Retrieve the current book instance
        context['average_rating'] = library.get_average_rating()