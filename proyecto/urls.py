"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import django

from django.conf import settings

# URLs de las distintas secciones de nuestra web
urlpatterns = [
    # Path del administrador
    url(r'^admin/', admin.site.urls),

    url(r'^viviendas/', include('viviendas.urls')),

    url(r'^politicas/', include('politicas.urls')),

    url(r'^contacto/', include('contacto.urls')),

    url(r'^nosotros/', include('nosotros.urls')),

    # Paths de las secciones de la web
    url(r'^', include('web.urls')),
]

# Ver archivos multimedia en modo DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom titles for admin
admin.site.site_header = "Mamja"
admin.site.index_title = "Panel de administrador"
admin.site.site_title = "Mamja"