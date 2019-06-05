from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SightingForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def sighting_form(request):
    if request.method == 'POST':
        print(request)
    else:
        form = SightingForm()
    return render(request, 'birdbird/sighting_form.html', {'form': form})

@login_required
def map(request):
    return render(request, 'birdbird/map.html')