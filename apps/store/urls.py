from django.urls import path
from .views import CategoryDetail, ProductDetailView, ProductList

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('category/<slug:slug>/', CategoryDetail.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view())
]