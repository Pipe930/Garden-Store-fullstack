from django.urls import path
from apps.administration.views.login.views import LoginFormView

urlsAdministration = [
    path("auth/login", LoginFormView.as_view(), name="login")
]
