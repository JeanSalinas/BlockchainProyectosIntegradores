from django.shortcuts import render, redirect
from  .usuario import Usuarios

# Create your views here.
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
def registro_usuario(request):
    if request.method == 'POST':
        nombres=request.POST['nombres']
        apellidos=request.POST['apellidos']
        tipo_documento=request.POST['tipo_documento']
        numero_documento=request.POST['numero_identificacion']
        numero_universidad=request.POST['numero_universidad']
        correo_institucional=request.POST['email_insitucional']
        contrasena=request.POST['contraseña']
        rol="1"
        ciclo="1"
        usuario = Usuarios(nombres, apellidos, correo_institucional, tipo_documento, numero_documento, numero_universidad, contrasena, rol, ciclo)
        usuario.set_usuario()
        return redirect('')

        







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