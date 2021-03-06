from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now= datetime.datetime.now()
    #render a template ,template name-"newyear/index.html
    return render(request,"newyear/index.html",{
        "newyear" : now.month==1 and now.day==1
    })
 