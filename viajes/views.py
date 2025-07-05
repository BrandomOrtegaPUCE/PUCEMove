from rest_framework import viewsets, status, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Viaje, Solicitud, PerfilUsuario
from .serializers import ViajeSerializer, SolicitudSerializer, UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):  # Solo lectura
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = ['id', 'username', 'email', 'tipo_usuario']

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(conductor=self.request.user)


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

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
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
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
    
@api_view(['POST'])
@permission_classes([AllowAny])
def registro_usuario(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    tipo_usuario = request.data.get('tipo_usuario')

    if not all([username, email, password, tipo_usuario]):
        return Response({'error': 'Todos los campos son obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    # El perfil se crea automáticamente por la señal
    perfil = PerfilUsuario.objects.get(user=user)
    perfil.tipo_usuario = tipo_usuario
    perfil.save()

    return Response({'mensaje': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)