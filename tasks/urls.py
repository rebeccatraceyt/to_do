from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_view, name='board_view'),
    path('add_task/', views.add_task, name='add_task'),
    path('archive_task/<int:task_id>/', views.archive_task, name='archive_task'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]
