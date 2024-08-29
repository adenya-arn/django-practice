from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def home (request, *args, **kwargs):
    return render (request, 'home.html' , {})
