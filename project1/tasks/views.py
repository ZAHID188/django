from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#global variable
#tasks=[]
# if we put global task variable everyone will have the same tasks 
#but we want different task for different people so it will be in the index



class NewTaskForm(forms.Form):
    task= forms.CharField(label="New Task")
    

# Create your views here.
def index(request):
    #this is for same person using same task new client will have new tasks list
    if "tasks" not in request.session:
        request.session["tasks"]=[]

    return render(request,"tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method =="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"] +=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else :
            return render(request,"tasks/add.html",{
            "form":form
        })

    return render(request,"tasks/add.html", {
        "form":NewTaskForm()

    })
     