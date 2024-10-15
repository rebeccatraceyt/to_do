from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_board, name='task_board'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('create_task/', views.create_task, name='create_task'),
    path('update_task/<int:pk>/', views.update_task, name='update_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('archived_tasks/', views.archived_tasks, name='archived_tasks'),
    path('update_task_archive/<int:task_id>/', views.update_task_archive, name='update_task_archive'),
    path('unarchive_task/<int:task_id>/', views.unarchive_task, name='unarchive_task'),
]
