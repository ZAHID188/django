from django.shortcuts import render
from .models import Flights
# Create your views here.
def index(request):
     return render(request,"flights/index.html",{
         "flights":Flights.objects.all()
     })

def flight(request,flight_id):
    flight= Flights.objects.get(pk=flight_id) #instead of id django use pk=primary key
    return render(request,"flights/flight.html",{
        "flight": flight,
        "pass":flight.passengers.all()
    })