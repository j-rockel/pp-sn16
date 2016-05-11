from django.shortcuts import render

def todo_list(request):
    return render(request, 'todo/todo_list.html', {})

def todo_edit(request):
    return render(request, 'todo/todo_edit.html', {})

def todo_add(request):
    return render(request, 'todo/todo_add.html', {})

def todo_impr(request):
    return render(request, 'todo/todo_impr.html', {})