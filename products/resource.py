from import_export import resources 
from .models import Category, Product

class CategoryResource(resources.ModelResource):
     class Meta:
         model = Category

class ProductResource(resources.ModelResource):
     class Meta:
         model = Product
