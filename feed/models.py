from django.contrib.auth.models import AbstractUser
from django.db import models


WEBSITE_TYPES = [("WEBSITE", "Website"), ("SHOP", "Shop"), ("SOCIAL", "Social")]
CATEGORY_TYPES = [("COMPANY", "Company"), ("BLOGGER", "Blogger")]


class User(AbstractUser):
    profile_photo = models.ImageField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Company(Common):
    signature = models.UUIDField()
    logo = models.ImageField()
    name = models.CharField(max_length=120)
    details = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Location(Common):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    town = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    def __str__(self):
        return self.lat, self.long, self.country


class Website(Common):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=20, choices=WEBSITE_TYPES)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Feed(Common):
    name = models.CharField(max_length=100)
    code = models.UUIDField()

    def __str__(self):
        return self.name


class Category(Common):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=CATEGORY_TYPES)

    def __str__(self):
        return self.name
