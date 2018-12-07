# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Vivienda, Vivienda_gallery

# Register your models here.


class ViviendaAdmin(admin.ModelAdmin):
    readonly_fields = ('publicacion', 'actualizacion')
    list_display = ('titulo', 'activado', 'tipo', 'operacion', 'ciudad', 'publicacion', 'id', 'destacado', 'imagen', 'planos')
    search_fields = ('activado', 'titulo', 'tipo', 'publicacion')
    ordering = ('-publicacion',)
    list_filter = ('activado', 'tipo', 'ciudad')


class ViviendaGalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('publicacion',  'actualizacion')
    list_display = ('id', 'publicacion', 'imagen_gallery')
    ordering = ('-publicacion',)


admin.site.register(Vivienda, ViviendaAdmin)
admin.site.register(Vivienda_gallery, ViviendaGalleryAdmin)

