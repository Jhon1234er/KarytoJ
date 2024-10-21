from django.shortcuts import render, redirect
from django.db import connection

#Son la capa que se comunica entre el HTML y el 
#MTV (Model, Template View)

def home(request):
    return render (request,'Home.html')