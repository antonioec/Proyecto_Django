# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Vivienda
from django.shortcuts import render, redirect, get_object_or_404, reverse
from forms import BusquedaForm

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.


class ViviendaDetailView(DetailView):
    model = Vivienda


class ViviendasListView(ListView):
    model = Vivienda
    template_name = "viviendas/viviendas.html"

    def get(self, request, *args, **kwargs):
        busqueda_form = BusquedaForm()

        viviendas = Vivienda.objects.filter(activado=True)

        return render(request, self.template_name, {'viviendas': viviendas, 'form': busqueda_form})

    def post(self, request, *args, **kwargs):
        busqueda_form = BusquedaForm(request.POST)
        if busqueda_form.is_valid():
            viviendas = Vivienda.objects.filter(activado=True)

            if request.POST['identificador']:
                identificador = request.POST['identificador']
                viviendas = viviendas.filter(id=identificador)

            if request.POST['operacion']:
                operacion = request.POST['operacion']
                viviendas = viviendas.filter(operacion=operacion)

            if request.POST['dormitorios']:
                dormitorios = request.POST['dormitorios']
                viviendas = viviendas.filter(dormitorios=dormitorios)

            if request.POST['premin']:
                premin = request.POST['premin']
                viviendas = viviendas.filter(precio__gte=premin)

            if request.POST['premax']:
                premax = request.POST['premax']
                viviendas = viviendas.filter(precio__lte=premax)

            if request.POST['ciudad']:
                ciudad = request.POST['ciudad']
                viviendas = viviendas.filter(ciudad=ciudad)

            if request.POST['tipo']:
                tipo = request.POST['tipo']
                viviendas = viviendas.filter(tipo=tipo)

            if request.POST['banos']:
                banos = request.POST['banos']
                viviendas = viviendas.filter(banos=banos)

            if request.POST['supmin']:
                supmin = request.POST['supmin']
                viviendas = viviendas.filter(superficie_construida__gte=supmin)

            if request.POST['supmax']:
                supmax = request.POST['supmax']
                viviendas = viviendas.filter(superficie_construida__lte=supmax)

            return render(request, self.template_name, {'viviendas': viviendas, 'form': busqueda_form})
