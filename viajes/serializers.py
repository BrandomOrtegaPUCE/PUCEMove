from rest_framework import serializers
from .models import Usuario, Viaje


class UsuarioSerializer(serializers.ModelSerializer):
    tipo_usuario_display = serializers.CharField(source='get_tipo_usuario_display', read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'tipo_usuario', 'tipo_usuario_display']


class ViajeSerializer(serializers.ModelSerializer):
    conductor = UsuarioSerializer(read_only=True)  # Mostrar info del conductor
    conductor_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), source='conductor', write_only=True)

    class Meta:
        model = Viaje
        fields = ['id', 'conductor', 'conductor_id', 'origen', 'destino', 'fecha', 'hora', 'cupos_disponibles']
