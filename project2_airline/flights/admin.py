from django.contrib import admin
from .models import Flights,Airport,Passenger
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)
admin.site.register(Airport)
admin.site.register(Flights,FlightAdmin)
admin.site.register(Passenger,PassengerAdmin)
