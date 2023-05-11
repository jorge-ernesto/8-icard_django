'''
Modificando el modelo del usuario
'''
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Reemplaza el campo utilizado para el logueo y la creacion de usuario, por defecto es "username", lo reeplaza por "email"
    REQUIRED_FIELDS = []

    # Si queremos crear un usuario con el comando "python manage.py createsuperuser",
    # debemos indicar que el campo "username" es requerido, ya que este campo es "NOT NULL UNIQUE",
    # lo que significa que no puede ser "NULL", y que no puede repetirse un string vacio
    # REQUIRED_FIELDS = ['username']
