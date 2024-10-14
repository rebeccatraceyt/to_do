from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm
from django.http import JsonResponse

def board_view(request):
    tasks = Task.objects.filter(is_archived=False).order_by('status')
    categories = Category.objects.all()
    return render(request, 'board.html', {'tasks': tasks, 'categories': categories})

def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    new_status = request.POST.get('status')
    if new_status in ['todo', 'in_progress', 'complete']:
        task.status = new_status
        task.save()
    return JsonResponse({'status': 'success'})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_view')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def archive_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_archived = True
    task.save()
    return redirect('board_view')
