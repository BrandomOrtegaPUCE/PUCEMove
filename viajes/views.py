from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import User, Viaje, Solicitud, PerfilUsuario
from .serializers import UsuarioSerializer, ViajeSerializer, SolicitudSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

    def perform_update(self, serializer):
        solicitud = serializer.save()
        viaje = solicitud.viaje

        # Validar si el usuario que hace la acción es docente
        perfil = PerfilUsuario.objects.get(user=self.request.user)
        if solicitud.estado != 'pendiente' and perfil.tipo_usuario != 'docente':
            raise ValidationError('Solo los docentes pueden aceptar o rechazar solicitudes.')

        # Si se acepta, verificar cupos
        if solicitud.estado == 'aceptada':
            if viaje.pasajeros.count() >= viaje.cupos_disponibles:
                raise ValidationError('No hay cupos disponibles en este viaje.')

            if solicitud.usuario not in viaje.pasajeros.all():
                viaje.pasajeros.add(solicitud.usuario)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if not user:
            return Response({'error': 'Credenciales inválidas'}, status=400)

        token, created = Token.objects.get_or_create(user=user)
        perfil = PerfilUsuario.objects.get(user=user)

        return Response({
            'token': token.key,
            'usuario_id': user.id,
            'username': user.username,
            'tipo_usuario': perfil.tipo_usuario
        })
        
@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def perfil_usuario(request):
    perfil = PerfilUsuario.objects.get(user=request.user)

    if request.method == 'GET':
        return Response({
            'username': request.user.username,
            'email': request.user.email,
            'tipo_usuario': perfil.tipo_usuario
        })

    if request.method == 'PATCH':
        perfil.tipo_usuario = request.data.get('tipo_usuario', perfil.tipo_usuario)
        perfil.save()
        return Response({'mensaje': 'Perfil actualizado correctamente'})