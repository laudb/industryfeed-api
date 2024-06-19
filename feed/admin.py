from django.contrib import admin
from .models import User, Company, Feed, Location, Website


class UserAdmin(admin.ModelAdmin):
    fields = ["username", "profile_photo", "country", "created_at"]


class CompanyAdmin(admin.ModelAdmin):
    fields = ["logo", "name", "is_active", "created_at"]


class FeedAdmin(admin.ModelAdmin):
    fields = ["name", "owner", "created_at"]


class LocationAdmin(admin.ModelAdmin):
    pass


class WebsiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Website, WebsiteAdmin)
