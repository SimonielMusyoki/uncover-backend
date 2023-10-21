from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .renderers import CategoryJSONRenderer, ProductsJSONRenderer, ProductJSONRenderer
from .serializers import CategorySerializer, ProductSerializer


class ProductList(APIView):
    def get(self, request, format=None):
        products = (Product.objects
                    .select_related("category")
                    .prefetch_related("productimage_set")
                    .prefetch_related("additionalinformation_set")
                    .prefetch_related("rating_set")
                    .all())
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):
    def get_object(self, slug):
        try:
            return (Product.objects
                    .select_related("category")
                    .prefetch_related("productimage_set")
                    .prefetch_related("additionalinformation_set")
                    .prefetch_related("rating_set")
                    .get(slug=slug))
        except Product.DoesNotExist:
            raise  NotFound({"message": "Product not found"})

    def get(self, request, slug, format=None):
        product = self.get_object(slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    renderer_classes = [CategoryJSONRenderer]
    def get_object(self, slug):
        try:
            return (Category.objects
                    .prefetch_related("product_set")
                    .get(slug=slug))
        except Category.DoesNotExist:
            raise NotFound({"message": "Category does not exist"})

    def get(self, request, slug, format=None):
        category = self.get_object(slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
