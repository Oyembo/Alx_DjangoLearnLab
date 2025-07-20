from django.shortcuts import render, redirect
from .models import Library
from models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        FORM = UserCreationForm(request.POST)
        if form.is_valid()
        user= form.save()
        login(request, user)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

@login required
def login_success_view(request):
    return render(request, 'relationship_app/login.html')

def logout_view(request):
    return render(request, 'relationship_app/logout.html')

@login_required
@user_passes_test(is_admin, login_url='/auth/login/') # Redirect to login if not admin
def admin_view(request):
    """View only accessible to users with the 'Admin' role."""
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/auth/login/') # Redirect to login if not librarian
def librarian_view(request):
    """View only accessible to users with the 'Librarian' role."""
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/auth/login/') # Redirect to login if not member
def member_view(request):
    """View only accessible to users with the 'Member' role."""
    return render(request, 'relationship_app/member_view.html')
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