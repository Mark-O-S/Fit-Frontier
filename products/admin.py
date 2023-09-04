from django.contrib import admin
from .models import Product, Category
from import_export.admin import ImportExportModelAdmin
from .resource import CategoryResource, ProductResource

# Register your models here.

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'available',
        'stock'
    )

    resource_class = ProductResource

    ordering = ('sku',)

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    resource_class = CategoryResource

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
