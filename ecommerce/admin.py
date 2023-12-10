from django.contrib import admin
from .models import Product, Order
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'stock', 'image_tag']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile','created_date']

