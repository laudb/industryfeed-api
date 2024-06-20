from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Company, Feed, Location, User, Website
from .serializers import (
    CompanySerializer,
    FeedSerializer,
    LocationSerializer,
    UserSerializer,
    WebsiteSerializer,
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
    permission_classes = [permissions.IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that creates, reads, updates, deletes a Location.
    """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoints that creates, read, updates deletes a User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that creates, reads, updates, deletes a Website.
    """

    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.IsAuthenticated]
