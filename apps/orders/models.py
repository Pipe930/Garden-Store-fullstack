from django.db import models
from uuid import uuid4
from apps.users.models import User
from apps.cart.models import Voucher

# Region Model
class Region(models.Model):

    name_region = models.CharField(max_length=60)
    initials = models.CharField(max_length=8)

    class Meta:

        db_table = 'regions'
        verbose_name = 'region'
        verbose_name_plural = 'regions'

    def __str__(self) -> str:
        return self.name_region

# Province Model
class Province(models.Model):

    name_province = models.CharField(max_length=40)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:

        db_table = 'provinces'
        verbose_name = 'province'
        verbose_name_plural = 'provinces'

    def __str__(self) -> str:
        return self.name_province

# Model Commune
class Commune(models.Model):

    name_commune = models.CharField(max_length=40)
    id_province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:

        db_table = 'communes'
        verbose_name = 'commune'
        verbose_name_plural = 'communes'

    def __str__(self) -> str:
        return self.name_commune

CHOICES_WITHDRAWAL = [
    ("Retiro en Tienda", "Retiro en Tienda"),
    ("Envio a Domicilio", "Envio a Domicilio")
]

CHOICES_CONDITION = [
    ("En Preparacion", "En Preparacion"),
    ("En Reparto", "En Reparto"),
    ("En Camino", "En Camino"),
    ("Entregado", "Entregado")
]

# Model Order
class Order(models.Model):

    code = models.UUIDField(default=uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=20, choices=CHOICES_CONDITION, default="En Preparacion")
    withdrawal = models.CharField(max_length=20, choices=CHOICES_WITHDRAWAL)
    direction = models.CharField(max_length=100)
    num_department = models.PositiveSmallIntegerField(blank=True, null=True)
    id_commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    id_voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self) -> str:
        return self.id_user.username
