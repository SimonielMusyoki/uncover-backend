import uuid
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.store.models import Product

User = settings.AUTH_USER_MODEL


class Order(models.Model):
    PAYMENT_STATUS_PENDING = "Pending"
    PAYMENT_STATUS_COMPLETE = "Complete"
    PAYMENT_STATUS_FAILED = "Failed"
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, PAYMENT_STATUS_PENDING),
        (PAYMENT_STATUS_COMPLETE, PAYMENT_STATUS_COMPLETE),
        (PAYMENT_STATUS_FAILED, PAYMENT_STATUS_FAILED),
    ]
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(
        max_length=10, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    delivery_address = models.TextField(verbose_name=_("Delivery Address"))
    delivery_name = models.CharField(max_length=50, verbose_name=_("Name"), blank=True)
    phone_number = models.CharField(max_length=13, verbose_name=_("Phone Number"))
    additional_delivery_instructions = models.TextField(
        verbose_name=_("Additional Delivery Instructions"), blank=True, null=True
    )
    payment_type = models.TextField(max_length=10, verbose_name=_("Payment Type"))

    def __str__(self) -> str:
        return f"Order No: -{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=20)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=20)
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=13)
    country = CountryField(verbose_name=_("country"), default="KE")
    city = models.CharField(verbose_name=_("City"), max_length=30, default="Nairobi")
    street_address = models.CharField(verbose_name=_("Street, Estate"), max_length=20)
    building = models.CharField(verbose_name=_("Bulding, Door Number"), max_length=50)
    is_default = models.BooleanField(verbose_name=_("Default Address"), default=False)

    class Meta:
        unique_together = ["user", "is_default"]

    def __str__(self) -> str:
        return f'{self.street_address}, {self.building}'
