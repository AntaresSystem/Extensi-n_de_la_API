from django.test import TestCase
from .models import Tarea
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

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

class TareaAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.tarea_data = {
            'titulo': 'Tarea API',
            'descripcion': 'Descripción API',
            'completado': False
        }

    def test_usuario_autenticado_puede_crear_tarea(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/tareas/', self.tarea_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_usuario_no_autenticado_no_puede_crear_tarea(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/tareas/', self.tarea_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
