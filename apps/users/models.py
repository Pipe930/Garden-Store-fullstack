from typing import Tuple
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

# Class to create users
class UserManager(BaseUserManager):

    # Method of creating a new user
    def _create_user(self, username, email, first_name, last_name, password, is_staff, is_superuser, **extra_fields):

        #The user model is instantiated
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        user.set_password(password) # Password is encrypted
        user.save(using = self.db) # The new user is saved in the database

        return user

    # Method of creating a user
    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password, False, False, **extra_fields)

    # Method of creating a superuser
    def create_superuser(self, username, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password, True, True, **extra_fields)

# User Model
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField('Correo', max_length=255, unique=True)
    first_name = models.CharField('Nombre', max_length=20, blank=True, null=True, default="(Sin Nombre)")
    last_name = models.CharField('Apellido', max_length=20, blank=True, null=True, default="(Sin Apellido)")
    date_joined = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def natural_key(self) -> Tuple[str]:
        return (self.username,)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

# Subscription Model
class Subscription(models.Model):

    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    mount = models.PositiveIntegerField()
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:

        db_table = "subscriptions"
        verbose_name = 'subscripcion'
        verbose_name_plural = 'subscripciones'

    def __str__(self) -> str:
        return self.username
