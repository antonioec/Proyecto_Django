# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Vivienda, Vivienda_gallery

# Register your models here.

class ViviendaAdmin(admin.ModelAdmin):
    readonly_fields = ('publicacion',)
    list_display = ('titulo', 'tipo', 'operacion', 'ubicacion', 'publicacion', 'id', 'destacado', 'imagen')
    search_fields = ('titulo', 'tipo', 'publicacion')
    ordering = ('publicacion',)
    list_filter = ('tipo', 'ubicacion')

class ViviendaGalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('publicacion',)
    list_display = ('titulo', 'publicacion', 'imagen_gallery')
    search_fields = ('titulo',)
    ordering = ('titulo', 'publicacion')
    list_filter = ('titulo',)

admin.site.register(Vivienda_gallery, ViviendaGalleryAdmin)
admin.site.register(Vivienda, ViviendaAdmin)