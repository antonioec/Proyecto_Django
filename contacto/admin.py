# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Contacto, Comentarios

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Clientes").exists():
            return ('publicacion', 'actualizacion', 'tipo')
        else:
            return ('publicacion', 'actualizacion')

    list_display = ('tipo', 'valor')
    ordering = ('id',)

class ComentariosAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre', 'email', 'comentario', 'publicacion',)
    list_display = ('nombre', 'email', 'publicacion',)

admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Contacto, ContactoAdmin)