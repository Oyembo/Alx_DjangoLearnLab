from django.urls import path
from .views import BookList
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
urlpatterns = router.urls

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

