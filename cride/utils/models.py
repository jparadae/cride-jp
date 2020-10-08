"""Django models utilities."""

# Django
from django.db import models


class ComparteRideModel(models.Model):
    """ComparteRideModel  base model.
     ComparteRideModel actúa como una clase base abstracta de la cual cada
     otro modelo en el proyecto heredará. Esta clase proporciona
     cada tabla con los siguientes atributos:
         + created (DateTime): almacena la fecha y hora en que se creó el objeto.
         + modified (DateTime): almacena la última fecha y hora en que se modificó el objeto.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Fecha y hora en la que se creo el objeto.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Fecha y hora de actualizacion del objeto.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
