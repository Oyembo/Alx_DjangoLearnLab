from django.urls import path
from .views import list_books
from django.views.generic.detail import LibraryDetailView
from django.contrib.auth. import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('login_success/', views.login_success_view, name='login_success'),
    path('logged_out/', views.logged_out_view, name='logged_out'),

    path('admin_dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian_dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member_dashboard/', views.member_view, name='member_dashboard'),

    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.BookCreateView.as_view(), name='book_add'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),

    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

