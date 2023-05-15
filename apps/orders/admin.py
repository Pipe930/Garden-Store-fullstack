from django.contrib import admin
from .models import Order, Region, Province, Commune

# Register models for panel control

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ["id_user", "condition", "withdrawal", "direction", "num_department"]
    list_filter = ["created"]
    ordering = ("created",)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):

    list_display = ["name_region", "initials"]
    list_filter = ["name_region"]
    ordering = ("name_region",)

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):

    list_display = ["name_province"]
    list_filter = ["id_region"]
    ordering = ("name_province",)

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):

    list_display = ["name_commune"]
    list_filter = ["id_province"]
    ordering = ("name_commune",)
