from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlsUser = [
    path("", views.UserListView.as_view()),
    path("user/<int:id>", views.DetailUserView.as_view()),
    path("register", views.RegisterUserView.as_view()),
    path("auth/login", views.LoginView.as_view()),
    path("auth/logout", views.LogoutView.as_view()),
]

urlsUser = format_suffix_patterns(urlsUser)
