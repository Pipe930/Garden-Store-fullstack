from django.urls import path
from .views.login.views import LoginFormView, LogoutFormView
from .views.panel.views import PanelView

urlsAdministration = [
    path("auth/login", LoginFormView.as_view(), name="login"),
    path("auth/logout", LogoutFormView.as_view(), name="logout"),
    path("dashboard/", PanelView.as_view(), name="panel")
]
