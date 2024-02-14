from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Tabla de inicio de sesion de administradores
class Adminsesion(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return  str(self.id) + " " + self.username

# Tabla de contacto de clientes
class FormularioClientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField(max_length=100)
    motivo = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellido