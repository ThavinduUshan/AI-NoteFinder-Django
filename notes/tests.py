from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category


class NoteTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_note_list_get(self):
        url = reverse('note_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_list_post(self):
        url = reverse('note_list')
        data = {'title': 'Test Note', 'content': 'This is a test note.',
                'category': self.category.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_search_notes(self):
        url = reverse('search_notes')
        query = 'test'
        response = self.client.get(url, {'query': query})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryTests(APITestCase):
    def test_category_list_get(self):
        url = reverse('category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_list_post(self):
        url = reverse('category_list')
        data = {'name': 'New Category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
