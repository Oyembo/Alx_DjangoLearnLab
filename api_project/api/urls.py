from django.urls import path
from .views import BookList
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # This line routes requests to your API
]