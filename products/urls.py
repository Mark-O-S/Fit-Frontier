from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
