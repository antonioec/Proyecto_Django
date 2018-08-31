# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# html_base = """
# <h1>Proyecto Integrado</h1>
# <ul>
#     <li><a href="/">Home</a></li>
#     <li><a href="/about/">Acerca de</a></li>
# </ul>
# """

# Create your views here.
def home(request):
    #html_response = html_base + "<h1>Home</h1>"
    #for i in range(0,10):
        #html_response+="<p>Buenas tardes</p>"
    return render(request, "prueba/home.html")

def contacto(request):
    return render(request, "prueba/contacto.html")

def section(request):
    return render(request, "prueba/section.html")