from django.db import models

# Create your models here.
# Modelo de la tabla de usuarios para postgresql
class Usuario(models.Model):
    nombre= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_doc = models.CharField(max_length=50)
    doc_identidad = models.CharField(max_length=50)
    cod_universidad = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    rol_id = models.ForeignKey('Rol', on_delete=models.CASCADE) 
    ciclo = models.CharField(max_length=50)
# Modelo de la tabla de roles para postgresql
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)
#Modelo de tipo documento para postgresql
class TipoDocumento(models.Model):
    id_tipo_doc = models.AutoField(primary_key=True)
    tipo_doc = models.CharField(max_length=50)
#Modelo de poryecto para postgresql
class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100)
    ciclo = models.CharField(max_length=50)
    estudiante_uno = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='estudiante_uno')
    estudiante_dos = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='estudiante_dos')
    estudiante_tres = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='estudiante_tres')
    jurado_uno = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='jurado_uno')
    jurado_dos = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='jurado_dos')
    jurado_tres = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='jurado_tres')
    fecha_hora_entrega = models.DateTimeField()
    id_cadena_bloque = models.CharField(max_length=500)
#Modelo de calificacion para postgresql
class Calificaciones(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    calificacion = models.CharField(max_length=500)
    observaciones = models.CharField(max_length=5000)
    fecha = models.DateTimeField()
#Modelo de parametroSistema
class ParametroSistemas(models.Model):
    fecha_hora_entrega = models.DateTimeField()


