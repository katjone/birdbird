# Generated by Django 2.2.1 on 2019-06-03 17:25

from django.db import migrations, models
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('photo_url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('address', models.CharField(max_length=100)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('photo_url', models.CharField(blank=True, max_length=250, null=True)),
                ('bird', models.ForeignKey(on_delete=False, related_name='sightings', to='birdbird.Species')),
            ],
        ),
    ]
