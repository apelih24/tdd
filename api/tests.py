from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book


class ModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='alex')
        self.book_name = 'The game of thrones'
        self.book_author = 'George R. R. Martin'
        self.book = Book(name=self.book_name, author=self.book_author, owner=user)

    def test_model_can_create_a_book(self):
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='alex')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.book_data = {
            'name': 'The game of thrones',
            'author': 'George R. R. Martin',
            'owner': user.id
        }
        self.response = self.client.post(
            reverse('create'),
            self.book_data,
            format='json'
        )

    def test_api_can_create_a_new_book(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        respone = new_client.get(
            reverse('details', kwargs={'pk': 1}),
            format='json')
        self.assertEqual(respone.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_book(self):
        book = Book.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': book.id}),
            format='json'
        )
        print(type(response))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_a_book(self):
        book = Book.objects.get()
        change_books = {
            'name': 'New Realms',
            'author': 'Savlatore R.'
        }
        response = self.client.put(
            reverse('details', kwargs={'pk': book.id}),
            change_books,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_book(self):
        book = Book.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': book.id}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
