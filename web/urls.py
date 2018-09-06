
from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contacto/', views.contacto, name='contacto'),
    url(r'^seccion/(?P<vivienda_id>[0-9]+)/', views.section, name='seccion'),
]