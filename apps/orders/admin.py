from django.contrib import admin
from .models import Order, Region, Province, Commune, Branch

# Register models for panel control

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):

    list_display = ["name_branch", "business_name", "direction"]
    list_filter = ["name_branch"]
    ordering = ("name_branch",)
    list_per_page = 20

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ["condition", "withdrawal", "direction", "num_department"]
    list_filter = ["created"]
    ordering = ("created",)
    list_per_page = 20

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):

    list_display = ["name_region", "initials"]
    list_filter = ["name_region"]
    ordering = ("name_region",)
    list_per_page = 20

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):

    list_display = ["name_province"]
    list_filter = ["id_region"]
    ordering = ("name_province",)
    list_per_page = 20

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):

    list_display = ["name_commune"]
    list_filter = ["id_province"]
    ordering = ("name_commune",)
    list_per_page = 20
