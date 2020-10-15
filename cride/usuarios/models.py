"""Modelo Usuarios"""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilidades
from cride.utils.models import ComparteRideModel


class User(ComparteRideModel, AbstractUser):
    """Redefiniendo el modelo original de django
    
    Se extiente utilizando el AbstracUser de django, cambiando el campo de autenticacion de user
    por email y agregando campos extra
    
    Reglas: 
    -Ningun usuario esta verificado inicialmente
    -Se validan las expr regulares del campo telefono con una instancia de RegexValidator
      
    """

    email = models.EmailField(
        'email address',
        unique= True,
        error_messages = {
         'unique': 'El correo ingresado ya existe en Cride-JP' 
        }
    )
     
    telefono_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        meesage='El formato de telefono debe ser +56999999999'
    )

    telefono = models.CharField(validators=[telefono_regex],max_length=17, ${blank=True})
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

    def __str__(self):
        """Retornando al usuario con el campo username"""
        return self.username 

    def get_short_name(self):
        """Retornando el campo username"""
        return self.username