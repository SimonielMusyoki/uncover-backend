import os
import random
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from apps.store.models import Product


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    _, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return f"content/sliders/{slugify(instance.name)}/{final_filename}"

def upload_page_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    _, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return f"pages/{slugify(instance.name)}/{final_filename}"


class HomepageSlider(models.Model):
    name = models.CharField(verbose_name=_("Image Name"), max_length=10)
    image = models.ImageField(upload_to=upload_image_path, verbose_name=_("Image"))
    landing_page = models.URLField(verbose_name=_("URL"))
    active = models.BooleanField(default=True, verbose_name=_("Active Status"))

    class Meta:
        verbose_name_plural = "Homepage Sliders"


class Page(models.Model):
    name = models.CharField(verbose_name=_("Page Name"), max_length=20, )
    slug = models.SlugField()
    seo_text = models.TextField(verbose_name=_("SEO Text"), max_length=50)
    banner = models.ImageField(upload_to=upload_page_image_path,blank=True, null=True)
    page_html = models.TextField(verbose_name=_("HTML Code"))
    featured_products = models.ManyToManyField(Product, verbose_name=_("Products on the page"))

    def __str__(self):
        return f'{self.name}'


class FlyoutMenuItem(models.Model):
    label = models.CharField(max_length=15)
    landing_page = models.URLField()

    def __str__(self):
        return f'{self.label}'
    class Meta:
        verbose_name_plural = "Flyout Menu"


class HomepageProductFloor(models.Model):
    title = models.CharField(max_length=20, verbose_name=_("Title"))
    landing_page = models.URLField(blank=True, null=True, verbose_name=_("Landing page"))
    has_countdown = models.BooleanField(default=False, verbose_name=_("Countdown Present"))
    countdown_enddate = models.DateTimeField(blank=True, null=True, verbose_name=_("Countdown End Time"))
    products = models.ManyToManyField(Product, verbose_name=_("Products on this widget"))
    active = models.BooleanField(default=True, verbose_name=_("Active Status"))

    class Meta:
        verbose_name_plural = "Homepage ProductFloors"
