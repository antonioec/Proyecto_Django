# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

# Create your models here.

def custom_upload_to(instance, filename):
    try:
        old_instance = instance.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return "projects/logotipo/" + filename
    except:
        return "projects/logotipo/" + filename

def custom_upload_to_mobile(instance, filename):
    try:
        old_instance = instance.objects.get(pk=instance.pk)
        old_instance.imagen_mobile.delete()
        return "projects/logotipo/" + filename
    except:
        return "projects/logotipo/" + filename

@python_2_unicode_compatible
class Logotipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    imagen = models.ImageField(verbose_name="Logotipo (Máx. 10MB)", upload_to=custom_upload_to)
    imagen_mobile = models.ImageField(verbose_name="Logotipo pequeño (Máx. 10MB)", upload_to=custom_upload_to_mobile, null=True)
    publicacion = models.DateField(verbose_name="Publicación", default=now)
    actualizacion = models.DateField(verbose_name="Actualización", auto_now=True)

    class Meta:
        verbose_name = "Logotipo"
        verbose_name_plural = "Logotipos"

    def __str__(self):
        return self.nombre