
from django.contrib import admin
from django.urls import path, include
from apps.users.urls import urlsUser
from apps.products.urls import urlsCategory, urlsProduct

urlsApi =  [
    path("users/", include(urlsUser)),
    path("categories/", include(urlsCategory)),
    path("products/", include(urlsProduct)),
]

urlpatterns = [
  path('admin/', admin.site.urls),
  path("api/v1/", include(urlsApi))
]
