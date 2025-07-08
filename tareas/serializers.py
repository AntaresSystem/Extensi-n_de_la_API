from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Tarea.
    
    Permite la serialización y deserialización de objetos Tarea.
    El campo usuario se establece automáticamente como solo lectura.
    """
    usuario = serializers.ReadOnlyField(
        source='usuario.username',
        help_text="Nombre de usuario del propietario de la tarea"
    )
    estado = serializers.ReadOnlyField(
        help_text="Estado de la tarea como texto (Completada/Pendiente)"
    )
    
    class Meta:
        model = Tarea
        fields = ['id', 'usuario', 'titulo', 'descripcion', 'completado', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        read_only_fields = ['id', 'usuario', 'fecha_creacion', 'fecha_actualizacion', 'estado']
        
    def validate_titulo(self, value):
        """
        Valida que el título no esté vacío y tenga un formato adecuado.
        """
        if not value.strip():
            raise serializers.ValidationError("El título no puede estar vacío")
        return value.strip()
    
    def validate_descripcion(self, value):
        """
        Valida que la descripción no esté vacía.
        """
        if not value.strip():
            raise serializers.ValidationError("La descripción no puede estar vacía")
        return value.strip() 