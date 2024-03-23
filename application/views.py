from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def mainpage(request):
    return render(request, "index.html")

def application(request):
    return HttpResponse("This request come from project urls -> application.urls -> application.views")


def about(request):
    return render(request, "about.html")