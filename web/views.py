# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from panel_control.models import Vivienda

# html_base = """
# <h1>Proyecto Integrado</h1>
# <ul>
#     <li><a href="/">Home</a></li>
#     <li><a href="/about/">Acerca de</a></li>
# </ul>
# """

# Create your views here.
def home(request):
    viviendas = Vivienda.objects.all() # Coge todos los objetos del modelo de Vivienda
    return render(request, "web/home.html", {'viviendas':viviendas})

def contacto(request):
    return render(request, "web/contacto.html")

def section(request):
    return render(request, "web/section.html")