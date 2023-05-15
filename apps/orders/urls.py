from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlsOrders = [
    path("", views.ListOrdersView.as_view()),
    path("order/<int:id>", views.DetailOrderView.as_view()),
    path("created", views.CreateOrderView.as_view()),
    path("regions/", views.ListRegionsView.as_view()),
    path("provinces/<int:id>", views.ListProvincesView.as_view()),
    path("communes/<int:id>", views.ListCommunesView.as_view()),
]

urlsOrders = format_suffix_patterns(urlsOrders)
