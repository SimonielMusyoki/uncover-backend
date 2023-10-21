from django.urls import path
from .views import SlidersView, FlyoutMenuView, ProductFloorsView, PageView

urlpatterns = [
    path("sliders/", SlidersView.as_view()),
    path("menu/",FlyoutMenuView.as_view()),
    path("floors/", ProductFloorsView.as_view()),
    path("pages/<slug:slug>/", PageView.as_view()),
]