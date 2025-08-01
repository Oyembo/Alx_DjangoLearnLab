from django.urls import path
from django.contrib.auth. import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='logged_out'), name='logout'),
    path('login_success/', views.login_success_view, name='login_success'),
    path('logged_out/', views.logged_out_view, name='logged_out'),
]

