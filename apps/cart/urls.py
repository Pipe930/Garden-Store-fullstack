from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlsCart = [
    path("user/<int:idUser>", views.CartUserView.as_view()),
    path("create", views.CreateCartView.as_view()),
    path("item/add", views.AddCartItemView.as_view()),
    path("item/substract", views.SubtractCartItemView.as_view()),
    path("clear/<int:id>", views.ClearCartItemsView.as_view())
]

urlsVoucher = [
    path("created", views.CreateVoucherView.as_view()),
    path("cancel/<int:id>", views.CancelPurchaseView.as_view()),
    path("user/<int:id>", views.ListVouchersView.as_view()),
    path("<int:id>", views.DetailVoucherView.as_view()),
]

urlsCart = format_suffix_patterns(urlsCart)
