from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from bookshelf.models import Book
from .serializers import BookSerializer

#create your views here

class BookListCreateView(generics.ListCreateAPIView):
    """
    Generic view to list all books or create a new one.
    
    GET /api/books/ - Retrieves a list of all books.
    POST /api/books/ - Creates a new book. (Requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # This permission class allows authenticated users to create new books,
    # while unauthenticated users can only view the list.

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view to retrieve, update, or delete a single book.
    
    GET /api/books/<int:pk>/ - Retrieves a single book.
    PUT/PATCH /api/books/<int:pk>/ - Updates a book. (Requires authentication)
    DELETE /api/books/<int:pk>/ - Deletes a book. (Requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # This permission class allows authenticated users to update/delete books,
    # while unauthenticated users can only retrieve a single book.

