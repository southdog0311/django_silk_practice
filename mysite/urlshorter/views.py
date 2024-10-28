from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse
from .models import Shorter
from .forms import ShorterForm
import json

def home_view(request):
    template = 'urlshorter/home.html'
    
    return render(request, template)

def redirect_url_view(request, shorted_part):
    try:
        shorter = Shorter.objects.get(short_url=shorted_part)
        shorter.times_followed += 1
        shorter.save()
        return HttpResponseRedirect(shorter.long_url)
    except Shorter.DoesNotExist:
        raise Http404('Sorry, this link is broken :(')

def api_shorten_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            long_url = data.get('long_url')

            form = ShorterForm(data={'long_url': long_url})
            if form.is_valid():
                shorted_object = form.save()
                new_url = request.build_absolute_uri('/') + shorted_object.short_url
                return JsonResponse({'new_url': new_url, 'long_url': shorted_object.long_url}, status=201)
            else:
                return JsonResponse({'errors': form.errors}, status=422)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def short_url_list_view(request):
    short_urls = Shorter.objects.all()
    context = {'short_urls': short_urls}
    return render(request, 'urlshorter/short_url_list.html', context)
    