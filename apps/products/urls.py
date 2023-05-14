from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Urls Views Categories
urlsCategory = [
    path("", views.ListCategoriesView.as_view()),
    path("category/<int:id>", views.CategoryDetailView.as_view()),
]

# Urls Views Products
urlsProduct = [
    path("", views.ListProductsView.as_view()),
    path("product/<str:slug>", views.ProductView.as_view()),
    path("search/product", views.ProductSearchView.as_view()),
    path("filter/<int:id>", views.ProductFilterView.as_view()),
    path("offer", views.ListProductOfferView.as_view()),
]

urlsCategory = format_suffix_patterns(urlsCategory)
urlsProduct = format_suffix_patterns(urlsProduct)
