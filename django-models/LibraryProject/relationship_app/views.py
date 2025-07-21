from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from .models import Library

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.forms import ModelForm

from .models import Book, Library, Author, Librarian, UserProfile, UserRole

def is_admin(user):
    if not user.is_authenticated:
        return False
    try:
        return user.profile.role == UserRole.ADMIN
    except UserProfile.DoesNotExist:
        return False

def is_librarian(user):
    if not user.is_authenticated:
        return False
    try:
        return user.profile.role == UserRole.LIBRARIAN
    except UserProfile.DoesNotExist:
        return False

def is_member(user):
    if not user.is_authenticated:
        return False
    try:
        return user.profile.role == UserRole.MEMBER
    except UserProfile.DoesNotExist:
        return False

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # UserProfile will be created automatically by the signal (in signals.py)
            login(request, user)
            return redirect('login_success')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

@login_required
def login_success_view(request):
    return render(request, 'relationship_app/login.html')

def logged_out_view(request):
    return render(request, 'relationship_app/logout.html')

@login_required
@user_passes_test(is_admin, login_url='/auth/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/auth/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/auth/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book_list')

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book_list')

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['book_count'] = library.books.count()
        return context
