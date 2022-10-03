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
    return render(request, 'formularios/vistasEstudiantes/registro.html',{
        "title":"Registro"
    })
def inicioAdministrador_views(request):
    return render(request, 'formularios/vistasAdministrador/inicioAdministrador.html',{
        "title":"Inicio Administrador"
    })
def inicioEstudiante_views(request):
    return render(request, 'formularios/vistasEstudiantes/inicioEstudiante.html',{
        "title":"Inicio Estudiante"
    })
def inicioProfesor_views(request):
    return render(request, 'formularios/vistasProfesor/inicioProfesor.html',{
        "title":"Inicio Profesor"
    })
def perfilEstudiante_views(request):
    return render(request, 'formularios/vistasEstudiantes/perfilEstudiante.html',{
        "title":"Perfil Estudiante"
    })
def perfilProfesor_views(request):
    return render(request, 'formularios/vistasProfesor/perfilProfesor.html',{
        "title":"Perfil Profesor"
    })
def perfilAdministrador_views(request):
    return render(request, 'formularios/vistasAdministrador/perfilAdministrador.html',{
        "title":"Perfil Administrador"
    })
def registroGrupo_views(request):
    return render(request, 'formularios/vistasEstudiantes/registroGrupo.html',{
        "title":"Registro Grupo"
    })
def registroProyecto_views(request):
    return render(request, 'formularios/vistasEstudiantes/registroProyecto.html',{
        "title":"Registro Proyecto Integrador"
    })
# def recuperarPass_views(request):
#     return render(request, 'formularios/recuperarPass.html',{
#         "title":"Recuperar Contraseña"
#     })
# def nuevaPass_views(request):
#     return render(request, 'formularios/nuevaPass.html',{       
#         "title":"Nueva Contraseña"                                
#     })

