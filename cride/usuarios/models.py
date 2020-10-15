"""Modelo Usuarios"""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser

#Utilidades
from cride.utils.models import ComparteRideModel


class User(ComparteRideModel, AbstractUser):
    """Redefiniendo el modelo original de django
    
    Se extiente utilizando el AbstracUser de django, cambiando el campo de autenticacion de user
    por email y agregando campos extra
    
    Reglas: Ningun usuario esta verificado inicialmente
    """

    email = models.EmailField(
        'email address',
        unique= True,
        error_message = {
         'unique': 'El correo ingresado ya existe en Cride-JP' 
        }
    )

    telefono = models.CharField(max_length=17, ${blank=True})
    is_client = models.BooleanField(
        'client status',
        default = True,
        help_text = (
            'Este campo sirve para identificar los admin de la plataforma cride-jp',
            'los clientes son un tipo de usuario'
        )
    )

    is_verified = models.BooleanField(
        'verificacion',
        default = True,
        help_text = 'Usuario creado y correo verificado con éxito'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']