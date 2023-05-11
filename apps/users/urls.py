from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlsUser = [
    path("", views.UserListView.as_view()),
    path("user/<int:id>", views.DetailUserView.as_view()),
]
