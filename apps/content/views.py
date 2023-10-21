from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status

from .models import HomepageSlider, HomepageProductFloor, FlyoutMenuItem, Page
from .serializers import SliderSerializer, ProductFloorSerializer, FlyoutMenuSerializer, PageSerializer
class SlidersView(APIView):
    def get(self, request, format=None):
        sliders = HomepageSlider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response({"status": status.HTTP_200_OK, "sliders": serializer.data})

class FlyoutMenuView(APIView):
    def get(self, request, format=None):
        fom = FlyoutMenuItem.objects.all()
        serializer = FlyoutMenuSerializer(fom, many=True)
        return Response({"status": status.HTTP_200_OK, "menu_items": serializer.data})

class ProductFloorsView(APIView):
    def get(self, request, format=None):
        product_floors = HomepageProductFloor.objects.prefetch_related('products')
        serializer = ProductFloorSerializer(product_floors,many=True)
        return Response({"status": status.HTTP_200_OK, "product_floors": serializer.data})

class PageView(APIView):
    def get(self, request, slug,format=None):
        page = Page.objects.get(slug=slug)
        serializer = PageSerializer(page, many=False)
        return Response({"status": status.HTTP_200_OK, "data": serializer.data})
