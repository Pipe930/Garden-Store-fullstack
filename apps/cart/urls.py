from django.urls import path, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlsCart = [
    path("user/<int:idUser>", views.CartUserView.as_view()),
    path("create", views.CreateCartView.as_view()),
    path("item/add", views.AddCartItemView.as_view()),
    path("item/substract", views.SubtractCartItemView.as_view()),
    path("clear/<int:id>", views.ClearCartItemsView.as_view()),
    path("delete/product/<int:id_cart>/<int:id_product>", views.DeleteProductCartView.as_view())
]

urlsVoucher = [
    path("created", views.CreateVoucherView.as_view()),
    path("cancel/<int:id>", views.CancelPurchaseView.as_view()),
    path("user/<int:id>", views.ListVouchersView.as_view()),
    path("<int:id>", views.DetailVoucherView.as_view()),
]

urlsCart = format_suffix_patterns(urlsCart)
