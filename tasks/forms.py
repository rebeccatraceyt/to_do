# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'due_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
