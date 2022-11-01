from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import TodoForm
from todo.models import Todo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    todos = []
    if request.user.is_authenticated:
        todos=Todo.objects.filter(user=request.user)
    form = TodoForm()
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'todo/home.html', context)

@login_required(login_url='login_user')
def todo_create(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'Todo Created Succesfully')
            return redirect('home')
    context ={
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)
@login_required(login_url='login_user')
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
    
@login_required(login_url='login_user')
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
    