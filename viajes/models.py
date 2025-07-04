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

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha} - {self.hora})"
