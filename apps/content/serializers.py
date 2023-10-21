from rest_framework import serializers

from .models import HomepageSlider, HomepageProductFloor, FlyoutMenuItem, Page
from apps.store.serializers import ProductSerializer
from apps.store.models import Product


class SliderSerializer(serializers.ModelSerializer):
    def get_image(self, obj: HomepageSlider):
        return obj.image.url

    class Meta:
        model = HomepageSlider
        fields = ['name', 'image', 'landing_page']


class FlyoutMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlyoutMenuItem
        fields = ['label', 'landing_page']


class ProductFloorSerializer(serializers.ModelSerializer):
    countdown_enabled = serializers.SerializerMethodField()
    countdown_end_date = serializers.SerializerMethodField()
    featured_products = serializers.SerializerMethodField()

    def get_featured_products(self, obj: HomepageProductFloor):
        products = (Product.objects
                    .prefetch_related("productimage_set")
                    .prefetch_related("additionalinformation_set")
                    .prefetch_related("rating_set")
                    .filter(id__in=obj.products.all()))
        serializer = ProductSerializer(products, many=True)
        return serializer.data

    def get_countdown_enabled(self, obj: HomepageProductFloor):
        return obj.has_countdown

    def get_countdown_end_date(self, obj: HomepageProductFloor):
        end_date = obj.countdown_enddate
        formatted_date_time = end_date.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date_time

    class Meta:
        model = HomepageProductFloor
        fields = ['title', 'landing_page', 'countdown_enabled', 'countdown_end_date', 'featured_products']


class PageSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()
    featured_products = serializers.SerializerMethodField()

    def get_html(self, obj: Page):
        return obj.page_html

    def get_featured_products(self, obj: Page):
        products = (Product.objects
                    .prefetch_related("productimage_set")
                    .prefetch_related("additionalinformation_set")
                    .prefetch_related("rating_set")
                    .filter(id__in=obj.featured_products.all()))
        serializer = ProductSerializer(products, many=True)
        return serializer.data

    def get_banner(self, obj: Page):
        return obj.banner.url

    class Meta:
        model = Page
        fields = ['name', 'slug', 'seo_text', 'banner', 'html', 'featured_products']
