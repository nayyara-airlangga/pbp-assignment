from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from todolist.forms import CreateTaskForm
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login')
def update_status(request, id):
    if request.method == "POST":
        if Task.objects.get(pk=id) is None:
            return HttpResponseNotFound("<h1>Task not found</h1>")

        task: Task = Task.objects.get(pk=id)
        Task.objects.filter(pk=id).update(is_finished=not task.is_finished)

        messages.success(request, f"Updated task status of task {id}")
        return redirect("todolist:todolist")

    res = HttpResponse("<h1>Method not allowed</h1>")
    res.status_code = 405

    return res


@login_required(login_url='/todolist/login')
def todolist(request):
    tasks = Task.objects.filter(user=request.user.pk)

    return render(
        request, 'todolist.html', context={'user': request.user, 'tasks': tasks}
    )


@login_required(login_url='/todolist/login')
def create_task(request):
    form = CreateTaskForm()

    if request.method == "POST":
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            form.save(request.user.id)
            messages.success(request, 'Task added successfully!')
            return redirect('todolist:todolist')

    context = {'form': form}
    return render(request, 'create-task.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created succesfully!')
            return redirect('todolist:login')

    context = {'form': form}

    return render(request, 'register.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            res = HttpResponseRedirect(reverse('todolist:todolist'))
            res.set_cookie('last_login', str(datetime.now()))

            return res
        else:
            messages.info(request, 'Incorrect username or password!')

    return render(request, 'login.html')


def user_logout(request):
    if request.method == "POST":
        logout(request)
        res = HttpResponseRedirect(reverse('todolist:login'))
        res.delete_cookie('last_login')
        return res

    return render(request, 'logout.html', context={'user': request.user})
