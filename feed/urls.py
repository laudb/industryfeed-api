from django.urls import path, include
from rest_framework.routers import DefaultRouter

from feed import views


router = DefaultRouter()
router.register(r"companies", views.CompanyViewSet, basename="company")
router.register(r"feeds", views.FeedViewSet, basename="feed")
router.register(r"websites", views.WebsiteViewSet, basename="website")
router.register(r"locations", views.LocationViewSet, basename="location")

urlpatterns = [
    path("", include(router.urls)),
]
