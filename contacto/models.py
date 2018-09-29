# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255, verbose_name="Tipo")
    valor = models.CharField(max_length=255, verbose_name="Contenido")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["-id"]

    def __str__(self):
        return self.tipo

class Comentarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField()
    publicacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-publicacion"]

    def __str__(self):
        return self.nombre
