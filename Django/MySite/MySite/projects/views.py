from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project


def home(request):
    return render(request, 'projects/home.html')


def aboutmyself(request):
    return render(request, 'projects/aboutmyself.html')


def contacts(request):
    return render(request, 'projects/contacts.html')


class ProjectsView(ListView):
    """Список проектов"""
    model = Project
    queryset = Project.objects.filter(draft=False)


class ProjectDetailView(DetailView):
    """Полное описание проекта"""
    model = Project
    slug_field = 'url'