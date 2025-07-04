from django.db import models

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('administrativo', 'Administrativo'),
    ]

    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_usuario})"


class Viaje(models.Model):
    conductor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='viajes_publicados')
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    cupos_disponibles = models.PositiveIntegerField()
    pasajeros = models.ManyToManyField(Usuario, related_name='viajes_como_pasajero', blank=True)

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha} - {self.hora})"


class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    mensaje = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.nombre} → {self.viaje} [{self.estado}]"
