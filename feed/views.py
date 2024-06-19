from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Company, Feed, Website, Location
from .serializers import (
    CompanySerializer,
    FeedSerializer,
    WebsiteSerializer,
    LocationSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that creates, reads, updates, deletes a Company.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class FeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that creates, reads, updates, deletes a Feed.
    """

    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that creates, reads, updates, deletes a Website.
    """

    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that creates, reads, updates, deletes a Location.
    """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
