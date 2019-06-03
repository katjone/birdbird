from django.shortcuts import render
from .forms import SightingForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        print(request)
    else:
        form = SightingForm()
    return render(request, 'birdbird/sighting_form.html', {'form': form})
