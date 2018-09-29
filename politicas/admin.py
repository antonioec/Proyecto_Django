# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Politica
# Register your models here.

class PoliticaAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Clientes").exists():
            return ('nombre',)
        else:
            return ()

    list_display = ('nombre', 'contenido')
    ordering = ('id',)

admin.site.register(Politica, PoliticaAdmin)