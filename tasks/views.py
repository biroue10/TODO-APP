from django.shortcuts import render, redirect
from .models import *
from .form import *
# Create your views here.


def index(request):
    task = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        'task': task,
        'form': form,
    }

    return render(request, 'tasks/list.html', context)


def update(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        'form': form
    } 

    return render(request, 'tasks/update.html', context)


def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect("/")
