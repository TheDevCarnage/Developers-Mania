import logging

from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
logger = logging
logger.basicConfig(filename="views.py", encoding="utf-8", level=logging.DEBUG)


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    try:
        project_obj = Project.objects.get(id=pk)
        context = {"project": project_obj}
        return render(request, "projects/single-project.html", context)
    except Exception:
        print(Exception)
    return


def create_project(request):
    try:
        form = ProjectForm()
        if request.method == "POST":
            logger.info("Validating all the fields of form")
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()

                logger.info(f"Record for project {form} added succesfully")
                return redirect("projects")
        context = {"form": form}
        return render(request, "projects/project_forms.html", context)
    except Exception as e:
        raise Exception(e)


def update_project(request, pk):
    try:
        project = Project.objects.get(id=pk)
        form = ProjectForm(instance=project)
        if request.method == "POST":
            logger.info("Validating all the fields of form.")
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                logger.info(f"Record for project {form} updated succesfully.")
                logger.info("Redirecting user to the projects page.")
                return redirect("projects")
        context = {"form": form}
        return render(request, "projects/project_forms.html", context)
    except Exception as e:
        raise Exception(e)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        title = project.title
        project.delete()
        print(f"Project {title} deleted successfully.")
        return redirect("projects")
    context = {"object": project}
    return render(request, "projects/delete_template.html", context)
