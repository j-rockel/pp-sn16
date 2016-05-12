from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect


def todo_list(request):
    todos = Todo.objects.all
    return render(request, 'todo/todo_list.html', {'todos' : todos})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form})

def todo_add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_add.html', {'form' : form})

def todo_impr(request):
    return render(request, 'todo/todo_impr.html', {})

def todo_del(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    Todo.objects.get(pk=pk).delete()
    return redirect("todo_list")
