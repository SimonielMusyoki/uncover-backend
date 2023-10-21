from rest_framework import serializers
from .models import Category, Product, ProductImage, Rating, AdditionalInformation


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    def get_banner(self, obj: Category):
        return obj.banner.url

    def get_icon(self, obj: Category):
        return obj.icon.url

    def get_products(self, obj: Category):
        products = obj.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ["id", "name", "parent_category", "slug", "seo_text", "banner", "icon", "active", "has_children", "products"]


class ProductImagesSerializer(serializers.ModelSerializer):
    def get_image(self, obj: ProductImage):
        return obj.image.url

    class Meta:
        model = ProductImage
        fields = [
            "image"
        ]


class RatingsSerializer(serializers.ModelSerializer):
    def get_rating(self, obj: Rating):
        return obj.rating_value

    def get_user(self, obj: Rating):
        return f'{obj.user.first_name} {obj.user.last_name}'

    class Meta:
        model = Rating
        fields = ["user", "rating", 'review', 'date']


class AdditionalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInformation
        fields = ['label', 'value']


class ProductSerializer(serializers.ModelSerializer):
    carousel = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    additional_info = serializers.SerializerMethodField()

    def get_category(self, obj: Product):
        serializer = CategorySerializer(obj.category, many=False)
        return serializer.data

    def get_image(self, obj: Product):
        return obj.image.url

    def get_carousel(self, obj: Product):
        image_objects = obj.productimage_set.all()
        return [obj.image.url for obj in image_objects]

    def get_ratings(self, obj: Product):
        ratings = obj.rating_set.all()
        serializer = RatingsSerializer(ratings, many=True)
        return serializer.data

    def get_additional_info(self, obj:Product):
        add_info = obj.additionalinformation_set.all()
        serializer = AdditionalInformationSerializer(add_info, many=True)
        return serializer.data

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'category', 'short_description', 'image','carousel', 'original_price', 'sale_price',
                  'quantity', 'max_order_count', 'long_description', 'average_rating', 'rating_count', 'ratings', 'additional_info']
