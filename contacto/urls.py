from django.conf.urls import url

from . import views
from .views import ContactoTemplateView
urlpatterns = [
    url(r'^$', ContactoTemplateView.as_view(), name='contacto'),
]