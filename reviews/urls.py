from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>', views.product_review, name='product_review'),
]
