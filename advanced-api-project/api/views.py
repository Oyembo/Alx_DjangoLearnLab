from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from bookshelf.models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    A generic view for listing all books.
    
    - Handles GET requests.
    - Allows read-only access for all users.

    Filtering:
    - Example: /api/books/?title=The Lord of the Rings
    
    Searching:
    - Example: /api/books/?search=lord
    
    Ordering:
    - Example: /api/books/?ordering=-title (descending)
   """
class BookDetailView(generics.RetrieveAPIView):
    """
    A generic view for retrieving a single book instance.
    
    - Handles GET requests for a specific book by ID.
    - Allows read-only access for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

class BookCreateView(generics.CreateAPIView):
    """
    A generic view for creating a new book.
    
    - Handles POST requests.
    - Requires an authenticated user to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    A generic view for updating an existing book.
    
    - Handles PUT and PATCH requests.
    - Requires an authenticated user to update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    A generic view for deleting an existing book.
    
    - Handles DELETE requests.
    - Requires an authenticated user to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]