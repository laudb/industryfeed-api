from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


# Create your models here.
class Company(models.Model):
    signature = models.UUIDField()
    logo = models.ImageField()
    name = models.CharField()
    details = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    town = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    def __str__(self):
        return self.lat, self.long, self.country


class Website(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=90)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Feed(models.Model):
    name = models.CharField(max_length=100)
    code = models.UUIDField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
