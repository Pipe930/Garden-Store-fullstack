from django.contrib import admin
from .models import User, Subscription
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register models for panel control

class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["username", "email", "is_active", "is_staff", "is_superuser"]
    list_per_page = 10

admin.site.register(User, UserAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    ordering = ["username"]
    list_display = ["username", "email", "mount"]

admin.site.register(Subscription, SubscriptionAdmin)
