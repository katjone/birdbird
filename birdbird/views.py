from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.conf import settings
from .forms import SightingForm
from .models import Sighting, Species
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def sighting_form(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            sighting = form.save(commit = False)
            sighting.observer = request.user
            sighting.save()
        return redirect('index')
    else:
        form = SightingForm()
        return render(request, 'birdbird/sighting_form.html', {'form': form})

@login_required
def map(request):

    # api_key = {'api_key': f'https://maps.googleapis.com/maps/api/js?key={settings.GOOGLE_MAPS_API_KEY}&callback=initMap'}
    # return render(request, 'birdbird/map.html', api_key)
    return render(request, 'birdbird/map.html')

def get_sightings(request):
    # sightings variable assigned to NameofModel, .function that gets all the rows on that Model's table
    # .values() turns row into an object consisting of key:value pairs
    sightings = Sighting.objects.values()
    sightings_with_bird = []
    for sighting in sightings:
        bird= Species.objects.get(pk=sighting['bird_id'])
        observer = User.objects.get(pk=sighting['observer_id'])
        sighting['bird_id'] = bird.name
        sighting['observer_id'] = observer.username
        sightings_with_bird.append(sighting)
     
    return JsonResponse({'sightings': list(sightings_with_bird)})

