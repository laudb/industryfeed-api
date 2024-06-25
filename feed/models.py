from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_photo = models.ImageField(null=True)
    phone_number = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100)

    @property
    def profile(self):
        return {
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "photo": self.profile_photo,
            "country": self.country
        }

    def __str__(self):
        return self.username


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(Common):
    signature = models.UUIDField()
    logo = models.ImageField()
    name = models.CharField(max_length=120)
    alias = models.CharField(max_length=120, blank=True, null=True)
    details = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Feed(Common):
    name = models.CharField(max_length=100)
    code = models.UUIDField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        null=True,
    )
    company = models.ManyToManyField(
        Company,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        return self.name


class Location(Common):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    town = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    @property
    def gps(self):
        "Returns latitude, longitude."
        return self.lat, self.long
    
    @property
    def address(self)
        "Returns country, state, town"
        return self.country, self.state, self.town

    def __str__(self):
        return self.country, self.lat, self.long


class Website(Common):
    WEBSITE_TYPES = [("WEBSITE", "Website"), ("SHOP", "Shop"), ("SOCIAL", "Social")]
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=20, choices=WEBSITE_TYPES)
    url = models.URLField(max_length=200)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        return self.name


class Category(Common):
    CATEGORY_TYPES = [("COMPANY", "Company"), ("BLOGGER", "Blogger")]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=CATEGORY_TYPES)

    def __str__(self):
        return self.name


class Post(Common):
    content = models.TextField()
    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        return f"{self.name}-{self.created_at}"
