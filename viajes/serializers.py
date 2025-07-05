from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Viaje, Solicitud, PerfilUsuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = ['id', 'username', 'email', 'tipo_usuario']


class ViajeSerializer(serializers.ModelSerializer):
    conductor = serializers.StringRelatedField(read_only=True)
    pasajeros = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Viaje
        fields = [
            'id', 'conductor', 'origen', 'destino',
            'fecha', 'hora', 'cupos_disponibles', 'pasajeros'
        ]

class SolicitudSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(source='usuario', queryset=User.objects.all(), write_only=True)
    viaje = serializers.StringRelatedField(read_only=True)
    viaje_id = serializers.PrimaryKeyRelatedField(source='viaje', queryset=Viaje.objects.all(), write_only=True)

    class Meta:
        model = Solicitud
        fields = ['id', 'usuario', 'usuario_id', 'viaje', 'viaje_id', 'estado', 'mensaje']