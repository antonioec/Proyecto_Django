from panel_control.models import Social, Destacado



def context_processors(request):
    ctx = {}
    social = Social.objects.all()
    for social in social:
        ctx[social.id] = social.link
    return ctx