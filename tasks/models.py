# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('library', '📖 Library'),
        ('assessments', '🗒️ Assessments'),
        ('kpi_tracker', '✨ KPI Tracker'),
        ('cohort', '📆 Cohort'),
        ('monthly_mscs', '🏆 Monthly MSCs'),
        ('task', '🎯 Task'),
        ('report', '📝 Report'),
        ('course_work', '📚 Course Work'),
        ('content_dev', '💡 Content'),
        ('content_dev', '🎨 Design'),
    ]
    STATUS_CHOICES = [
        ('todo', '🔴 To-Do'),
        ('in_progress', '🔵 In Progress'),
        ('complete', '🟢 Complete'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    archive = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)