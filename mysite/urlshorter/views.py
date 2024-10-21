from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Shorter
from .forms import ShorterForm

def home_view(request):
    template = 'urlshorter/home.html'
    context = {}
    context['form'] = ShorterForm()
    
    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = ShorterForm(request.POST)
        if used_form.is_valid():
            shorted_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shorted_object.short_url
            long_url = shorted_object.long_url
            context['new_url'] = new_url
            context['long_url'] = long_url
            return render(request, template, context)
        
        context['errors'] = used_form.errors
        return render(request, template, context)

        

def redirect_url_view(request, shorted_part):
    try:
        shorter = Shorter.objects.get(short_url=shorted_part)
        shorter.times_followed += 1
        shorter.save()
        return HttpResponseRedirect(shorter.long_url)
    except Shorter.DoesNotExist:
        raise Http404('Sorry, this link is broken :(')
