from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class TareaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar tareas de usuarios.
    
    Permite crear, leer, actualizar y eliminar tareas.
    Solo usuarios autenticados pueden acceder a sus propias tareas.
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completado', 'titulo']

    def perform_create(self, serializer):
        """Asigna automáticamente el usuario actual a la tarea creada."""
        serializer.save(usuario=self.request.user)

    def get_queryset(self):
        """Filtra las tareas para mostrar solo las del usuario actual."""
        return Tarea.objects.filter(usuario=self.request.user)

    @swagger_auto_schema(
        operation_description="Obtiene la lista de tareas del usuario autenticado",
        operation_summary="Listar tareas",
        manual_parameters=[
            openapi.Parameter(
                'completado',
                openapi.IN_QUERY,
                description="Filtrar por estado de completado (true/false)",
                type=openapi.TYPE_BOOLEAN,
                required=False
            ),
            openapi.Parameter(
                'titulo',
                openapi.IN_QUERY,
                description="Filtrar por título de la tarea",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'page',
                openapi.IN_QUERY,
                description="Número de página para paginación",
                type=openapi.TYPE_INTEGER,
                required=False
            ),
        ],
        responses={
            200: openapi.Response(
                description="Lista de tareas obtenida exitosamente",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'count': openapi.Schema(type=openapi.TYPE_INTEGER, description="Total de tareas"),
                        'next': openapi.Schema(type=openapi.TYPE_STRING, description="URL de la siguiente página"),
                        'previous': openapi.Schema(type=openapi.TYPE_STRING, description="URL de la página anterior"),
                        'results': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID de la tarea"),
                                    'usuario': openapi.Schema(type=openapi.TYPE_STRING, description="Nombre de usuario"),
                                    'titulo': openapi.Schema(type=openapi.TYPE_STRING, description="Título de la tarea"),
                                    'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description="Descripción de la tarea"),
                                    'completado': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Estado de completado"),
                                }
                            )
                        )
                    }
                )
            ),
            401: openapi.Response(description="No autenticado"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crea una nueva tarea para el usuario autenticado",
        operation_summary="Crear tarea",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['titulo', 'descripcion'],
            properties={
                'titulo': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Título de la tarea",
                    max_length=200
                ),
                'descripcion': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Descripción detallada de la tarea"
                ),
                'completado': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description="Estado de completado (opcional, por defecto false)"
                ),
            }
        ),
        responses={
            201: openapi.Response(
                description="Tarea creada exitosamente",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID de la tarea"),
                        'usuario': openapi.Schema(type=openapi.TYPE_STRING, description="Nombre de usuario"),
                        'titulo': openapi.Schema(type=openapi.TYPE_STRING, description="Título de la tarea"),
                        'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description="Descripción de la tarea"),
                        'completado': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Estado de completado"),
                    }
                )
            ),
            400: openapi.Response(description="Datos inválidos"),
            401: openapi.Response(description="No autenticado"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene los detalles de una tarea específica",
        operation_summary="Obtener tarea",
        responses={
            200: openapi.Response(
                description="Detalles de la tarea obtenidos exitosamente",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID de la tarea"),
                        'usuario': openapi.Schema(type=openapi.TYPE_STRING, description="Nombre de usuario"),
                        'titulo': openapi.Schema(type=openapi.TYPE_STRING, description="Título de la tarea"),
                        'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description="Descripción de la tarea"),
                        'completado': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Estado de completado"),
                    }
                )
            ),
            401: openapi.Response(description="No autenticado"),
            404: openapi.Response(description="Tarea no encontrada"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualiza una tarea existente",
        operation_summary="Actualizar tarea",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'titulo': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Título de la tarea",
                    max_length=200
                ),
                'descripcion': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Descripción detallada de la tarea"
                ),
                'completado': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description="Estado de completado"
                ),
            }
        ),
        responses={
            200: openapi.Response(
                description="Tarea actualizada exitosamente",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID de la tarea"),
                        'usuario': openapi.Schema(type=openapi.TYPE_STRING, description="Nombre de usuario"),
                        'titulo': openapi.Schema(type=openapi.TYPE_STRING, description="Título de la tarea"),
                        'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description="Descripción de la tarea"),
                        'completado': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Estado de completado"),
                    }
                )
            ),
            400: openapi.Response(description="Datos inválidos"),
            401: openapi.Response(description="No autenticado"),
            404: openapi.Response(description="Tarea no encontrada"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualiza parcialmente una tarea existente",
        operation_summary="Actualizar parcialmente tarea",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'titulo': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Título de la tarea",
                    max_length=200
                ),
                'descripcion': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Descripción detallada de la tarea"
                ),
                'completado': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description="Estado de completado"
                ),
            }
        ),
        responses={
            200: openapi.Response(
                description="Tarea actualizada parcialmente exitosamente",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID de la tarea"),
                        'usuario': openapi.Schema(type=openapi.TYPE_STRING, description="Nombre de usuario"),
                        'titulo': openapi.Schema(type=openapi.TYPE_STRING, description="Título de la tarea"),
                        'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description="Descripción de la tarea"),
                        'completado': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Estado de completado"),
                    }
                )
            ),
            400: openapi.Response(description="Datos inválidos"),
            401: openapi.Response(description="No autenticado"),
            404: openapi.Response(description="Tarea no encontrada"),
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Elimina una tarea existente",
        operation_summary="Eliminar tarea",
        responses={
            204: openapi.Response(description="Tarea eliminada exitosamente"),
            401: openapi.Response(description="No autenticado"),
            404: openapi.Response(description="Tarea no encontrada"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Marca una tarea como completada o no completada",
        operation_summary="Cambiar estado de completado",
        responses={
            200: openapi.Response(
                description="Estado de completado cambiado exitosamente",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID de la tarea"),
                        'usuario': openapi.Schema(type=openapi.TYPE_STRING, description="Nombre de usuario"),
                        'titulo': openapi.Schema(type=openapi.TYPE_STRING, description="Título de la tarea"),
                        'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description="Descripción de la tarea"),
                        'completado': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Nuevo estado de completado"),
                    }
                )
            ),
            401: openapi.Response(description="No autenticado"),
            404: openapi.Response(description="Tarea no encontrada"),
        }
    )
    @action(detail=True, methods=['post'])
    def toggle_completado(self, request, pk=None):
        """Acción personalizada para cambiar el estado de completado de una tarea."""
        tarea = self.get_object()
        tarea.completado = not tarea.completado
        tarea.save()
        serializer = self.get_serializer(tarea)
        return Response(serializer.data)
