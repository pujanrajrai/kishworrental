from django.db import models

# Create your models here.
from accounts.models import MyUser


class Vehicle(models.Model):
    owner = models.OneToOneField(MyUser, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20)
    vehicle = models.ImageField()
    km_driven = models.PositiveSmallIntegerField()
    seat = models.PositiveSmallIntegerField()
    price_per_day = models.CharField(max_length=100)
    wheeler = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    is_available = models.CharField(max_length=100, default=True)
