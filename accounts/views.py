from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from birdbird.models import Species, Sighting

# IMPORT DJANGO USER MODEL
from .models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check if username exists
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {'error': 'That username has already been registered. Please try a different username'})
            else:
                # Check if email exists
                if User.objects.filter(email=email).exists():
                    return render(request, 'accounts/register.html', {'error': 'That email has already been registered'})
                else:
                    # Register User
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid Credentials...'})

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required
def profile(request):
    user = request.user
    user_sightings = Sighting.objects.filter(observer_id = user.id)
    bird_ids = user_sightings.values('bird_id').distinct()
    birds = []
    for bird in bird_ids:
        bird_name = Species.objects.get(pk=bird['bird_id'])
        # observer = User.objects.get(pk=sighting['observer_id'])
        # sighting['bird_id'] = bird.name
        # sighting['observer_id'] = observer.username
        birds.append(bird_name)

    return render(request, 'accounts/profile.html', {'user': user, 'birds':birds, 'sightings': user_sightings})
