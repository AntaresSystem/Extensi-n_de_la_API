from django.shortcuts import render
from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer

# Create your views here.

class TareaListCreateView(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
