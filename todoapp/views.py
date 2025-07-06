# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return HttpResponse('Hello Idiots')
@login_required
def todo_list(request):
    if request.method == 'POST':
        task = request.POST.get('task-input')

        print(request.user)
        if task:
            new_task = models.Todo(task=task,user=request.user)
            new_task.save()
            messages.success(request, 'Add Task successfully')
            return redirect('todo_list')
    tasks = models.Todo.objects.filter(user=request.user)
    return render(request, 'todoapp/index.html',{'tasks': tasks})

def delete_task(request,pk):
    task= models.Todo.objects.get(pk=pk)
    if task:
        task.delete()
        messages.success(request, 'Task deleted successfully')
    return redirect('todo_list')

def delete_all_tasks(request):
    models.Todo.objects.all().delete()
    messages.success(request, 'All tasks deleted successfully')
    return redirect('todo_list')

def complete_task(request, pk): 
    task = get_object_or_404(models.Todo, pk=pk)
    if  task:
        task.completed = not task.completed
        task.save()
        return redirect('todo_list') 
    return render( request, 'todoapp/index.html', {'task': task} )

# registration and Log in 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        age = request.POST.get('age')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect( 'register')
        User.objects.create_user(username=username, password=password, email=email)
        Profile = models.Profile(name=username, password=password, email=email, age=age)
        Profile.save()

        messages.success(request, 'Profile created successfully')
        return redirect('login')
    return render(request, 'user/register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Log in successfully')
            return redirect('todo_list')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'user/login.html')


def logout(request):
    auth_logout(request)
    messages.success(request, 'Log Out Successfully')
    return redirect ('login')