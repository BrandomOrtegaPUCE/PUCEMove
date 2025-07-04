from rest_framework import viewsets
from .models import Usuario, Viaje, Solicitud
from .serializers import UsuarioSerializer, ViajeSerializer, SolicitudSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

    def perform_update(self, serializer):
        solicitud = serializer.save()

        # Si se acepta, agregar usuario a los pasajeros del viaje
        if solicitud.estado == 'aceptada':
            viaje = solicitud.viaje
            if solicitud.usuario not in viaje.pasajeros.all():
                viaje.pasajeros.add(solicitud.usuario)
                viaje.save()
