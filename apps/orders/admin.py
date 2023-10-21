from django.contrib import admin
from .models import Order, OrderItem
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def items_count(self, obj):
        return obj.order_items.count()

    list_display = [
        "pkid",
        "__str__",
        "customer",
        "phone_number",
        "delivery_name",
        "payment_type",
        "payment_status",
        "items_count",
    ]
    list_display_links = ["pkid", "__str__", "items_count"]
    list_per_page = 20
    list_filter = [
        "payment_type",
        "payment_status",
    ]
    search_fields = ["customer", "phone_number"]
    inlines = [OrderItemInline]
