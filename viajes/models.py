from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20)  # estudiante, docente, administrativo

    def __str__(self):
        return self.nombre

class Viaje(models.Model):
    conductor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    cupos_disponibles = models.IntegerField()

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha})"
