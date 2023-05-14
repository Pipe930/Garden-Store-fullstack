from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlsUser = [
    path("register", views.RegisterUserView.as_view()),
    path("auth/login", views.LoginView.as_view()),
    path("auth/logout", views.LogoutView.as_view()),
    path("subscriptions/", views.ListSubscriptionView.as_view()),
    path("subscription/created", views.CreateSubscriptionView.as_view()),
    path("subscriptions/user/<int:id>", views.SubscriptionDetailView.as_view()),
    path('sendEmail', views.SendEmailView.as_view()),
    path('change-password', views.ChangePasswordView.as_view()),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]

urlsUser = format_suffix_patterns(urlsUser)
