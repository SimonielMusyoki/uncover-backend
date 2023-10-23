from django.contrib import admin

from .models import Category, Product, ProductImage, AdditionalInformation, Rating

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'icon','parent_category', 'active']
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 20
    search_fields = ["name"]

class ProductImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class AdditionalInformation(admin.TabularInline):
    model = AdditionalInformation
    extra =  0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ["orders_count", "rating", "rating_count"]
    list_display = ['name', 'category', 'orders_count', 'sale_price', 'quantity', 'max_order_count', 'average_rating']
    inlines = [ProductImagesInline, AdditionalInformation]
    list_per_page = 20
    sortable_by = ['original_price','orders_count', 'sale_price','rating', 'quantity']
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]

admin.site.register(Rating)