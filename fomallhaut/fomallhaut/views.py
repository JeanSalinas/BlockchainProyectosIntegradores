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
def inicioAdministrador_views(request):
    return render(request, 'formularios/inicioAdmionistrador.html',{
        "title":"Inicio Administrador"
    })
def inicioEstudiante_views(request):
    return render(request, 'formularios/inicioEstudiante.html',{
        "title":"Inicio Estudiante"
    })
def inicioProfesor_views(request):
    return render(request, 'formularios/inicioProfesor.html',{
        "title":"Inicio Profesor"
    })
def perfilEstudiante_views(request):
    return render(request, 'formularios/perfilEstudiante.html',{
        "title":"Perfil Estudiante"
    })
def perfilProfesor_views(request):
    return render(request, 'formularios/perfilProfesor.html',{
        "title":"Perfil Profesor"
    })
def registroGrupo_views(request):
    return render(request, 'formularios/retgistroGrupo.html',{
        "title":"Registro Grupo"
    })
def registroProyecto_views(request):
    return render(request, 'formularios/registroProyecto.html',{
        "title":"Registro Proyecto Integrador"
    })


