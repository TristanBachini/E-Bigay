from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey
from django.core import validators


class City(models.Model):
    city = CharField(max_length=50, null=True)

    def __str__(self):
        return self.city


class Region(models.Model):
    REGIONS = [
        ('NCR', 'National Capital Region'),
        ('CAR', 'Cordillera Administrative Region'),
        ('Region I', 'Ilocos Region'),
        ('Region II', 'Cagayan Valley Region'),
        ('Region III', 'Central Luzon Region'),
        ('Region IV-A', 'CALABARZON Region'),
        ('Region IV-B', 'MIMAROPA Region'),
        ('Region V', 'Bicol Region'),
        ('Region VI', 'Western Visayas Region'),
        ('Region VII', 'Central Visayas Region'),
        ('Region VIII', 'Eastern Visayas Region'),
        ('Region IX', 'Zamboanga Peninsula Region'),
        ('Region X', 'Northern Mindanao Region'),
        ('Region XI', 'Davao Region'),
        ('Region XII', 'SOCCSKARGEN Region'),
        ('Region XIII', 'Caraga Region'),
        ('BARMM', 'Bangsamoro Autonomous Region in Muslim Mindanao')
    ]
    region = CharField(max_length=50, null=True, choices=REGIONS)

    def __str__(self):
        return self.region


class AyudaApplicant(models.Model):
    name = CharField(max_length=100, null=True)
    dateofbirth = DateField(null=True)
    city = ForeignKey(City, on_delete=models.CASCADE, null=True)
    street1 = CharField(max_length=100, null=True)
    street2 = CharField(max_length=100, null=True)
    region = ForeignKey(Region, on_delete=models.CASCADE, null=True)
    personid = models.ImageField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class AyudaDropoff(models.Model):
    ayudaapplicant = ForeignKey(
        AyudaApplicant, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ayudaapplicant.name


class CityChoice(models.Model):
    city = ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.city
