from django.shortcuts import render, redirect
from  .usuario import Usuarios
from .models import Usuario, Rol, TipoDocumento, Proyecto, Calificaciones, ParametroSistemas

# Vista de inicio de la página web
def index(request):
    return render(request, "index.html",{
        "title":"Inicio"
})
# Fin de inicio de la página web
# Logins de los usuarios y funciones
def login_views(request):
    return render(request, 'formularios/login.html', {
        'title': 'Login'
})
def login_sistema(request):
    if request.method == 'POST':
        correo_institucional=request.POST['email_institucional']
        contrasena=request.POST['contraseña']
        usuario = Usuario.objects.get(correo=correo_institucional, contrasena=contrasena)
        if usuario.rol_id_id == 1:
            return redirect('perfilEstudiante')
        elif usuario.rol_id_id == 2:
            return redirect('perfilProfesor')
        elif usuario.rol_id_id == 3:
            return redirect('perfilAdministrador')
        else:
            return redirect('login')
    else:
        return redirect('login')

# En esta vista se maneja el manejo de registro de los usuarios
def registro_views(request):
    return render(request, 'formularios/registro.html',{
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
        return redirect('login')
# Termina el manejo de registro de los usuarios

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