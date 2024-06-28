from django.contrib.auth.models import User
from .models import Company, Feed, Website, Location, Post
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "country"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["signature", "alias", "name", "details", "logo"]


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ["name", "code"]


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ["name", "type", "url"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["town", "state", "country", "lat", "long"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["company", "content"]
