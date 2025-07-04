from rest_framework import serializers
from .models import Usuario, Viaje, Solicitud


class UsuarioSerializer(serializers.ModelSerializer):
    tipo_usuario_display = serializers.CharField(source='get_tipo_usuario_display', read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'tipo_usuario', 'tipo_usuario_display']


class ViajeSerializer(serializers.ModelSerializer):
    conductor = UsuarioSerializer(read_only=True)
    conductor_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), source='conductor', write_only=True)
    pasajeros = UsuarioSerializer(many=True, read_only=True)

    class Meta:
        model = Viaje
        fields = ['id', 'conductor', 'conductor_id', 'origen', 'destino', 'fecha', 'hora', 'cupos_disponibles', 'pasajeros']


class SolicitudSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(source='usuario', queryset=Usuario.objects.all(), write_only=True)
    viaje = ViajeSerializer(read_only=True)
    viaje_id = serializers.PrimaryKeyRelatedField(source='viaje', queryset=Viaje.objects.all(), write_only=True)

    class Meta:
        model = Solicitud
        fields = ['id', 'usuario', 'usuario_id', 'viaje', 'viaje_id', 'estado', 'mensaje']
