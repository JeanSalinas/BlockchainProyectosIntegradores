# Generated by Django 4.1.1 on 2022-10-18 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParametroSistemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_entrega', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id_proyecto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(max_length=100)),
                ('ciclo', models.CharField(max_length=50)),
                ('estudiante_uno', models.CharField(max_length=50)),
                ('estudiante_dos', models.CharField(max_length=50)),
                ('estudiante_tres', models.CharField(max_length=50)),
                ('jurado_uno', models.CharField(max_length=50)),
                ('jurado_dos', models.CharField(max_length=50)),
                ('jurado_tres', models.CharField(max_length=50)),
                ('fecha_hora_entrega', models.DateTimeField()),
                ('id_cadena_bloque', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id_tipo_doc', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_doc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_doc', models.CharField(max_length=50)),
                ('doc_identidad', models.CharField(max_length=50)),
                ('cod_universidad', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('ciclo', models.CharField(max_length=50)),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projecto.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id_calificacion', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.CharField(max_length=500)),
                ('observaciones', models.CharField(max_length=5000)),
                ('fecha', models.DateTimeField()),
                ('id_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projecto.proyecto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projecto.usuario')),
            ],
        ),
    ]
