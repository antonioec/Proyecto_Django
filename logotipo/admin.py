# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Logotipo

# Register your models here.

class LogotipoAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Clientes").exists():
            return ('publicacion', 'actualizacion', 'nombre',)
        else:
            return ('publicacion', 'actualizacion')

    list_display = ('nombre', 'imagen', 'imagen_mobile')


admin.site.register(Logotipo, LogotipoAdmin)