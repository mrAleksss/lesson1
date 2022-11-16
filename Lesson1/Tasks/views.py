from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


tasks = ["get up", "wash", "eat"]


def index(request):
    return render(request, 'tasks/index.html', {'tasks': tasks})


def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks:add.html", {"form": NewTaskForm()})

    return render(request, 'tasks/add.html', {'form': NewTaskForm})