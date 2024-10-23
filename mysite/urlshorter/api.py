from ninja import NinjaAPI
from .models import Shorter
from .forms import ShorterForm
from django.http import Http404

api = NinjaAPI(urls_namespace="shortener_api")

@api.post("/shorten/")
def create_short_url(request, long_url: str):
    form = ShorterForm(data={'long_url': long_url})
    if form.is_valid():
        shorted_object = form.save()
        return {"new_url": request.build_absolute_uri('/') + shorted_object.short_url}
    else:
        return {"errors": form.errors}

@api.get("/{shorted_part}")
def get_long_url(request, shorted_part: str):
    try:
        shorter = Shorter.objects.get(short_url=shorted_part)
        return {"long_url": shorter.long_url}
    except Shorter.DoesNotExist:
        raise Http404('Sorry, this link is broken :(')

@api.get("/shortened/")
def get_shortened_urls(request):
    shorteners = Shorter.objects.all().values("long_url", "short_url")
    return {"shortened_urls": list(shorteners)}
