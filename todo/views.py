from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import TodoForm
from todo.models import Todo
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
            return redirect('home')
    context ={
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)

def todo_update(request,id):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={
        'form_update':form
    }
    return render(request, 'todo/todo_update.html', context)
    