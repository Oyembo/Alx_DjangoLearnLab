from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from bookshelf.models import Author, Book

#create your tests here

class BookAPITests(APITestCase):
    """
    Test suite for the BookListCreateView and BookDetailView API endpoints.
    
    This class uses Django's APITestCase to set up a test database and a client
    for simulating HTTP requests.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test user and some initial data.
        This method runs before every test case.
        """
        # Create a test user for authenticated requests
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )

        self.client.login(username='testuser', password='testpassword')

    def test_book_create_authenticated(self):
        # Now, this test will run with the client already logged in
        # and should pass if the view permissions are correctly set.
        pass
        
        # Create author and book instances for testing
        self.author1 = Author.objects.create(name='J.R.R. Tolkien')
        self.author2 = Author.objects.create(name='Stephen King')
        self.book1 = Book.objects.create(title='The Lord of the Rings', author=self.author1, publication_year=1954)
        self.book2 = Book.objects.create(title='The Hobbit', author=self.author1, publication_year=1937)
        self.book3 = Book.objects.create(title='The Shining', author=self.author2, publication_year=1977)

        # Define URLs for the API endpoints
        self.list_url = reverse('book-list-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})



    def test_book_list(self):
        """
        Ensure the book list view can retrieve all books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that all three books are returned
        self.assertEqual(len(response.data), 3)

    def test_book_create_authenticated(self):
        """
        Ensure a new book can be created by an authenticated user.
        """
        self.client.force_authenticate(user=self.user)
        new_author = Author.objects.create(name='George Orwell')
        data = {
            'title': '1984',
            'author': new_author.pk,
            'publication_year': 1949
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check that the new book was added to the database
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.get(title='1984').author, new_author)

    def test_book_create_unauthenticated(self):
        """
        Ensure a new book cannot be created by an unauthenticated user (permission check).
        """
        data = {
            'title': 'Animal Farm',
            'author': self.author1.pk,
            'publication_year': 1945
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 3)  # Ensure no new book was created

    def test_book_retrieve(self):
        """
        Ensure a single book can be retrieved by its primary key.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_book_update_authenticated(self):
        """
        Ensure an existing book can be updated by an authenticated user.
        """
        self.client.force_authenticate(user=self.user)
        updated_data = {'title': 'The Lord of the Rings (Updated)', 'author': self.book1.author.pk}
        response = self.client.put(self.detail_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Lord of the Rings (Updated)')

    def test_book_update_unauthenticated(self):
        """
        Ensure an existing book cannot be updated by an unauthenticated user.
        """
        updated_data = {'title': 'New Title', 'author': self.book1.author.pk}
        response = self.client.put(self.detail_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.book1.refresh_from_db()
        # Verify the title did not change
        self.assertNotEqual(self.book1.title, 'New Title')

    def test_book_delete_authenticated(self):
        """
        Ensure a book can be deleted by an authenticated user.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)
        # Check that the book no longer exists
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_book_delete_unauthenticated(self):
        """
        Ensure a book cannot be deleted by an unauthenticated user.
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Verify the book still exists
        self.assertTrue(Book.objects.filter(pk=self.book1.pk).exists())

    # --- Test Filtering, Searching, and Ordering ---

    def test_book_list_filter_by_title(self):
        """
        Ensure the book list can be filtered by title.
        """
        url = self.list_url + '?title=The Hobbit'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_book_list_search(self):
        """
        Ensure the book list can be searched by a term in the title or author name.
        """
        url = self.list_url + '?search=Tolkien'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return both Tolkien books
        # Check that the expected books are present in the response
        self.assertIn('The Lord of the Rings', [book['title'] for book in response.data])
        self.assertIn('The Hobbit', [book['title'] for book in response.data])
        
    def test_book_list_ordering(self):
        """
        Ensure the book list can be ordered by a specific field.
        """
        # Order by title descending
        url = self.list_url + '?ordering=-title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ['The Shining', 'The Lord of the Rings', 'The Hobbit'])



