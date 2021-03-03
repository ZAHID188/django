from django.urls import path
#from . means = same directory / the directory hello
from . import views


urlpatterns = [

    path("", views.index, name="index"),
    path("<str:name>",views.greet, name="greet"),
    path("zahid", views.zahid, name="zahid"),
    path("rayhan", views.rayhan, name="rayhan"),
    
]
