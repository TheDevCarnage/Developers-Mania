from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Projects(request):
    message = "You're in the Projects page"
    return render(request, "projects/projects.html", {"message": message})


def Project(request, pk):
    return render(request, "projects/single-project.html")
