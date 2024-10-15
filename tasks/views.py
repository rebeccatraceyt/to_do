# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_board')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_board')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_board')

@login_required
def task_board(request):
    tasks = Task.objects.filter(user=request.user, archive=False)
    todo_tasks = tasks.filter(status='todo')
    in_progress_tasks = tasks.filter(status='in-progress')
    complete_tasks = tasks.filter(status='complete')
    return render(request, 'tasks/task_board.html', {
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'complete_tasks': complete_tasks,
    })

@csrf_exempt
def update_task_status(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id)
            data = json.loads(request.body)
            new_status = data.get('status')

            if new_status in ['todo', 'in_progress', 'complete']:
                task.status = new_status
                task.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid status'})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def update_task_archive(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id)
            data = json.loads(request.body)
            archive_status = data.get('archive')

            task.archive = archive_status
            task.save()

            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def archived_tasks(request):
    # Filter tasks that are archived and belong to the current user
    archived_tasks = Task.objects.filter(archive=True, user=request.user)
    
    context = {
        'archived_tasks': archived_tasks
    }
    return render(request, 'tasks/archived_tasks.html', context)

@csrf_exempt
def unarchive_task(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id)
            data = json.loads(request.body)
            archive_status = data.get('archive')

            task.archive = archive_status  # Set archive to False
            task.save()

            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})