from .models import Usuario, Rol, TipoDocumento, Proyecto, Calificaciones, ParametroSistemas
class Usuarios:
    def __init__(self, nombre, apellidos, correo, tipo_doc, doc_identidad, cod_universidad, contrasena, rol, ciclo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.tipo_doc = tipo_doc
        self.doc_identidad = doc_identidad
        self.cod_universidad = cod_universidad
        self.contrasena = contrasena
        self.rol = rol
        self.ciclo = ciclo
    def set_usuario(self):
        usuario = Usuario(nombre=self.nombre, apellidos=self.apellidos, correo=self.correo, tipo_doc=self.tipo_doc, doc_identidad=self.doc_identidad, cod_universidad=self.cod_universidad, contrasena=self.contrasena, ciclo=self.ciclo, rol_id_id=self.rol)
        usuario.save()