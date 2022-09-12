from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Esto es una prueba de Django")
