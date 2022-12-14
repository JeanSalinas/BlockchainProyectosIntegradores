# Generated by Django 4.1.1 on 2022-10-18 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='estudiante_dos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiante_dos', to='projecto.usuario'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='estudiante_tres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiante_tres', to='projecto.usuario'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='estudiante_uno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiante_uno', to='projecto.usuario'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='jurado_dos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurado_dos', to='projecto.usuario'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='jurado_tres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurado_tres', to='projecto.usuario'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='jurado_uno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurado_uno', to='projecto.usuario'),
        ),
    ]
