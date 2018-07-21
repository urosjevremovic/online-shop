from django.contrib import admin

from shop.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', ]
    list_filter = ['available', 'created', 'updated', ]
    list_editable = ['price', 'available', 'stock', ]
    prepopulated_fields = {'slug': ('name', )}
