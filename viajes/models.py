from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    TIPO_CHOICES = [
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('administrativo', 'Administrativo'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.tipo_usuario})"


class Viaje(models.Model):
    conductor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viajes_publicados')
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    cupos_disponibles = models.PositiveIntegerField()
    pasajeros = models.ManyToManyField(User, related_name='viajes_como_pasajero', blank=True)

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha} - {self.hora})"


class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    mensaje = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} → {self.viaje} [{self.estado}]"
