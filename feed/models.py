from django.db import models


# Create your models here.
class Company(models.Model):
    pass


class Location(models.Model):
    pass


class Website(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=90)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


class Feed(models.Model):
    pass


class Category(models.Model):
    pass
