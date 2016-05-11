from django.shortcuts import render
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all
    return render(request, 'todo/todo_list.html', {'todos' : todos})

def todo_edit(request):
    return render(request, 'todo/todo_edit.html', {})

def todo_add(request):
    return render(request, 'todo/todo_add.html', {})

def todo_impr(request):
    return render(request, 'todo/todo_impr.html', {})