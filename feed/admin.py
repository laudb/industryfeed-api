from django.contrib import admin
from .models import User, Company, Feed, Location, Website


class UserAdmin(admin.ModelAdmin):
    fields = ["username", "profile_photo", "country"]


class CompanyAdmin(admin.ModelAdmin):
    fields = ["logo", "name", "is_active"]


class FeedAdmin(admin.ModelAdmin):
    fields = ["name", "owner", "company"]


class LocationAdmin(admin.ModelAdmin):
    pass


class WebsiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Website, WebsiteAdmin)
