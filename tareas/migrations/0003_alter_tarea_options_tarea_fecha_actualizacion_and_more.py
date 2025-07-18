# Generated by Django 5.2.2 on 2025-07-08 01:42

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_tarea_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarea',
            options={'ordering': ['-fecha_creacion'], 'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, help_text='Fecha y hora de la última actualización'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Fecha y hora de creación de la tarea'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarea',
            name='completado',
            field=models.BooleanField(default=False, help_text='Indica si la tarea ha sido completada'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(help_text='Descripción detallada de la tarea'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(help_text='Título descriptivo de la tarea', max_length=200),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='usuario',
            field=models.ForeignKey(help_text='Usuario propietario de la tarea', on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='tarea',
            table='tareas',
        ),
    ]
