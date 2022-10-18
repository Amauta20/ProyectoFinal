from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombres = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    nacimiento = models.CharField(max_length=10)

def __str__(self):
    return f"{self.nombres}, {self.numero_pasaporte}, {self.direccion}, {self.nacimiento}, {self.id}"

