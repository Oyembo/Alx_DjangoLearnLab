from django.shortcuts import render
from models import Book

# Create your views here.
def book_list(request):
    """Retrieves all books and renders a template displaying the list"""
    books = Book.objects.all()
    context = {'book list': books}
    return render(request, books/book_list.html)

class BookDetailView(DetailView):
    """A class-based view for displaying details of specific book."""
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book"""
        context = super().get_context_data(**kwargs) #Get default context data
        book = self.get_object() #Retrieve the current book instance
        context['average_rating'] = book.get_average_rating()