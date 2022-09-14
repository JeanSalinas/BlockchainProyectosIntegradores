# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html",{
        "title":"Inicio"
    })
def login_views(request):
    return render(request, 'formularios/login.html', {
        'title': 'Login'
    })
def registro_views(request):
    return render(request, 'formularios/registro.html',{
        "title":"Registro"
    })
