from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
