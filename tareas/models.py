from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    """
    Modelo para representar una tarea de usuario.
    
    Cada tarea pertenece a un usuario específico y puede tener
    un título, descripción y estado de completado.
    """
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='tareas',
        help_text="Usuario propietario de la tarea"
    )
    titulo = models.CharField(
        max_length=200,
        help_text="Título descriptivo de la tarea"
    )
    descripcion = models.TextField(
        help_text="Descripción detallada de la tarea"
    )
    completado = models.BooleanField(
        default=False,
        help_text="Indica si la tarea ha sido completada"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación de la tarea"
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de la última actualización"
    )

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-fecha_creacion']
        db_table = 'tareas'

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"

    @property
    def estado(self):
        """Retorna el estado de la tarea como texto."""
        return "Completada" if self.completado else "Pendiente"
