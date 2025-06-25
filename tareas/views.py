from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completado', 'titulo']

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
