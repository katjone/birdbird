from django.db import models
# from django.forms import ModelForm
from django.utils.timezone import now
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User


# Create your models here.
class Species(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    photo_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Sighting(models.Model):
    date = models.DateField(default=now)
    address = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=['address'], zoom=15)
    photo_url = models.CharField(max_length=250, blank=True, null=True)
    bird = models.ForeignKey(Species, on_delete=False, related_name='sightings')
    observer = models.ForeignKey(User, on_delete=False, related_name='sightings', default=1 )

    def __str__(self):
        return self.bird     

