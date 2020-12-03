from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "Site/index.html", {})


def team(request):

    return render(request, "Site/Team.html", {})


def project(request):
    return render(request, "Site/project.html", {})


def contact(request):
    return render(request, "Site/contact.html", {})


def about(request):
    return render(request, "Site/about.html", {})








