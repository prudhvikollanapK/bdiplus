from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskTests(APITestCase):

    def test_create_task(self):
        url = reverse('task-list-create')
        data = {'title': 'Test Task', 'description': 'Test Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tasks(self):
        url = reverse('task-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description')
        url = reverse('task-retrieve-update-destroy', kwargs={'pk': task.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description')
        url = reverse('task-retrieve-update-destroy', kwargs={'pk': task.id})
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'completed': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description')
        url = reverse('task-retrieve-update-destroy', kwargs={'pk': task.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_task_data(self):
        url = reverse('task-list-create')
        data = {'description': 'Test Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_non_existent_task(self):
        url = reverse('task-retrieve-update-destroy', kwargs={'pk': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)