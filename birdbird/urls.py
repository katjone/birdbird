from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sighting-form', views.sighting_form, name='sighting-form'),
    path('map', views.map, name='map'),
    path('get-sightings', views.get_sightings, name='get-sightings'),
]