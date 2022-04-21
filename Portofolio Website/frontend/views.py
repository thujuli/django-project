from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def home(request):
    listProject = Project.objects.all()
    context = {
        'listProject': listProject}
    return render(request, 'frontend/index.html', context)


def createPoject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'frontend/create-project.html', context)
