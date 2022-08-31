from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import TodoForm
from todo.models import Todo
from django.contrib import messages
# Create your views here.

def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'todo/home.html', context)

def todo_create(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo Created Succesfully')
            return redirect('home')
    context ={
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)

def todo_update(request,id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={
        'todo':todo,
        'form_update': form
    }
    return render(request, 'todo/todo_update.html', context)
    
    
def todo_delete(request,id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        messages.warning(request, 'Todo Deleted Succesfully')
        return redirect('home')
    context ={
        'todo':todo,
    }
    return render(request, 'todo/todo_delete.html', context)
    