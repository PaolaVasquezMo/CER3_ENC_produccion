from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Planta(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class RegistroProduccion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    litros_producidos = models.FloatField()
    fecha_produccion = models.DateField()
    turno_choices = [
        ('AM', 'Mañana'),
        ('PM', 'Tarde'),
        ('MM', 'Noche'),
    ]
    turno = models.CharField(max_length=2, choices=turno_choices)
    hora_registro = models.TimeField(auto_now_add=True)
    operador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto} - {self.fecha_produccion}"