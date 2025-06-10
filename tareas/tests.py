from django.test import TestCase
from .models import Tarea

# Create your tests here.

class TareaModelTest(TestCase):
    def test_creacion_tarea(self):
        tarea = Tarea.objects.create(
            titulo='Prueba',
            descripcion='Descripción de prueba',
            completado=False
        )
        self.assertEqual(tarea.titulo, 'Prueba')
        self.assertFalse(tarea.completado)
