# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import EmailMessage

from django.shortcuts import render, redirect
from django.urls import reverse
from forms import ContactForm
from models import Comentarios
from django.views.generic.base import TemplateView

# Create your views here.

# def contacto(request):
#     contact_form = ContactForm()
#
#     if request.method == "POST":
#         contact_form = ContactForm(request.POST)
#         if contact_form.is_valid():
#             try:
#                 newComment = Comentarios(nombre = request.POST['name'], email = request.POST['email'], comentario = request.POST['content'])
#                 email = EmailMessage(
#                     "(Proyecto) Nuevo mensaje de contacto",
#                     "De " + request.POST['name'] + " (" + request.POST['email'] + ")\n\nContenido del mensaje: \n" + request.POST['content'],
#                     request.POST['email'],
#                     ["proantonio1997@gmail.com"],
#                     reply_to=[request.POST['email']]
#                 )
#                 email.send()
#
#                 newComment.save()
#                 return redirect(reverse('contacto')+"?ok")
#             except:
#                 return redirect(reverse('contacto') + "?fail")
#
#     return render(request, "web/contacto.html", {"form":contact_form})

class ContactoTemplateView(TemplateView):
    template_name = "web/contacto.html"

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            try:
                newComment = Comentarios(nombre = request.POST['name'], email = request.POST['email'], comentario = request.POST['content'])
                email = EmailMessage(
                    "MAMJA - Nuevo mensaje de contacto",
                    "De " + request.POST['name'] + " (" + request.POST['email'] + ")\n\nContenido del mensaje: \n" + request.POST['content'],
                    request.POST['email'],
                    ["proantonio1997@gmail.com"],
                    reply_to=[request.POST['email']]
                )
                email.send()

                newComment.save()
                return redirect(reverse('contacto')+"?enviado")
            except:
                return redirect(reverse('contacto') + "?error")

    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        return render(request, self.template_name, {"form":contact_form})