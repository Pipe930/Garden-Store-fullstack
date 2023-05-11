
from django.contrib import admin
from django.urls import path, include
from apps.users.urls import urlsUser

urlsApi =  [
    path("users/", include(urlsUser))
]

urlpatterns = [
  path('admin/', admin.site.urls),
  path("api/v1/", include(urlsApi))
]
