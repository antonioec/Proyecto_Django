from social.models import Social
from carousel.models import Carousel
from viviendas.models import Vivienda
from contacto.models import Contacto
from politicas.models import Politica



def social_context_processors(request):
    sctx = {}
    social = Social.objects.all()
    for social in social:
        sctx[social.id] = social.link
    return sctx

def carousel_context_processors(request):
    carousel = Carousel.objects.all()
    return {'carousel':carousel}

def destacado_context_processors(request):
    destacado = Vivienda.objects.all().filter(destacado=True)
    return {'destacado':destacado}

def contacto_context_processors(request):
    contacto = Contacto.objects.all()
    return {'contacto':contacto}

def politica_context_processors(request):
    politicas = Politica.objects.all()
    return {'politicas':politicas}