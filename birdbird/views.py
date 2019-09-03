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
    sightings = Sighting.objects.values()

    for s in sightings:
        bird_id = s['bird_id']
        bird = Species.objects.get(pk = bird_id)
        s['bird_name'] = bird.name

        observer_id = s['observer_id']
        observer = User.objects.get(pk = observer_id)
        s['observer_name'] = observer.username
        print(s)

    return JsonResponse({'sightings': list(sightings)})
    
