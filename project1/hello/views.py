from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def zahid(request):
    return HttpResponse("hello zahid")
def rayhan(request):
    return HttpResponse(" hello, raihan")
def greet(request,name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()

    })
