from django.urls import path
from .views import task_list_create, task_retrieve_update_destroy


urlpatterns = [
    path('tasks/', task_list_create, name='task-list-create'),
    path('tasks/<int:pk>/', task_retrieve_update_destroy, name='task-retrieve-update-destroy'),
]
