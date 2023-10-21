from django.contrib import admin

from .models import HomepageSlider, FlyoutMenuItem, HomepageProductFloor, Page

@admin.register(HomepageSlider)
class HomepageSliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'landing_page', 'active']
    list_filter = ['active']
    list_per_page = 20

@admin.register(HomepageProductFloor)
class HomepageProductFloorAdmin(admin.ModelAdmin):
    list_display = ['title',  'landing_page', 'active', 'has_countdown']
    list_filter = ['active', 'has_countdown']
    list_per_page = 20

@admin.register(FlyoutMenuItem)
class FlyoutMenuItemsAdmin(admin.ModelAdmin):
    list_display = ['label', 'landing_page']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['name', 'landing_page']
    list_per_page = 20
