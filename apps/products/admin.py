from django.contrib import admin
from .models import Category, Offer, Product

# Register models for panel control

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ["name_category", "description"]


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):

    list_display = ["name_offer", "start_date", "end_date", "discount"]
    list_filter = ["start_date", "end_date"]
    ordering = ("name_offer",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ["name_product", "price", "stock", "description", "id_category", "id_offer"]
    list_filter = ["name_product", "price", "stock", "condition", "create"]
    exclude = ("slug", "create")
    ordering = ("name_product",)
