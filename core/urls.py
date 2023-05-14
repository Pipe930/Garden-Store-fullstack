
from django.contrib import admin
from django.urls import path, include
from apps.users.urls import urlsUser
from apps.products.urls import urlsCategory, urlsProduct
from apps.cart.urls import urlsCart, urlsVoucher

urlsApi =  [
    path("user/", include(urlsUser)),
    path("categories/", include(urlsCategory)),
    path("products/", include(urlsProduct)),
    path("cart/", include(urlsCart)),
    path("voucher/", include(urlsVoucher))
]

urlpatterns = [
  path('admin/', admin.site.urls),
  path("api/v1/", include(urlsApi))
]
