from django.urls import path
from feed import views

urlpatterns = [
    path("company/", views.CompanyViewSet),
    path("feed/", views.FeedViewSet),
    path("website/", views.WebsiteViewSet),
    path("location/", views.LocationViewSet),
]
