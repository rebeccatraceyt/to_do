from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)  # Store icon classes or paths

    def __str__(self):
        return f'Category: {self.icon} {self.friendly_name}'

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ]
    
    title = models.CharField(max_length=255)
    checklist = models.JSONField(default=list)  # Store checklist items as a list
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    due_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    is_archived = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
