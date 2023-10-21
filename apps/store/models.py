import os
import random
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from core.settings import AUTH_USER_MODEL


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_product_main_image_path(instance, filename):
    _, ext = get_filename_ext(filename)
    final_filename = f"{instance.slug}{ext}"
    return f"products/{instance.slug}/{final_filename}"


def upload_product_image_path(instance, filename):
    _, ext = get_filename_ext(filename)
    final_filename = f"{instance.product.slug}-{instance.id}{ext}"
    return f"products/{instance.product.slug}/{final_filename}"


class Category(models.Model):
    name = models.CharField(verbose_name=_("Category Name"), max_length=50)
    parent_category = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    seo_text = models.CharField(verbose_name=_('Category SEO Text'), max_length=255)
    banner = models.ImageField(verbose_name=_("Category Banner"), upload_to='categories/%Y/%m/%D', blank=True,
                               null=True)
    icon = models.ImageField(verbose_name=_("Category Icon"), upload_to='categories/%Y/%m/%D', blank=True, null=True)
    active = models.BooleanField(verbose_name=_("Activate Category"), default=True)
    has_children = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name=_("Product Name"), max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    short_description = RichTextField(verbose_name=_("Short Description"))
    image = models.ImageField(upload_to=upload_product_main_image_path)
    original_price = models.DecimalField(verbose_name=_("Original Price"), decimal_places=2, max_digits=10)
    sale_price = models.DecimalField(decimal_places=2, max_digits=10, blank=True,
                                     null=True)
    active = models.BooleanField(verbose_name=_("Show product on website"), default=True)
    quantity = models.IntegerField(verbose_name=_("Stock"))
    max_order_count = models.IntegerField(verbose_name=_("Max cart quantity"), blank=True, null=True)
    long_description = RichTextField(verbose_name=_("Long Description"))

    average_rating = models.DecimalField(verbose_name=_("Product Rating"), decimal_places=1, max_digits=3, default=0.0)
    rating_count = models.IntegerField(verbose_name=_("Number of rating"), default=0)
    orders_count = models.IntegerField(verbose_name=_("Number ordered"), default=0)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_product_image_path)


class AdditionalInformation(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Category"), on_delete=models.CASCADE)
    label = models.CharField(verbose_name=_("Label eg Weight"), max_length=15)
    value = models.CharField(verbose_name=_("Value eg 500g"), max_length=100)

    def __str__(self):
        return f"{self.label}: {self.value}"

    class Meta:
        verbose_name_plural = "Additional Information"


class Rating(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    rating_value = models.IntegerField(verbose_name=_("Rating Value"),
                                       validators=[MaxValueValidator(5), MinValueValidator(1)])
    review = models.CharField(verbose_name=_("Review"), max_length=20, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.__str__()} rated {self.rating_value} stars on {self.product.name}"

    class Meta:
        verbose_name_plural = "Ratings"
