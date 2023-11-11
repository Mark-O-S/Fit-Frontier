from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_wishlist, name='show_wishlist'),
    path('add_wishlist_product/<int:product_id>/', views.add_wishlist_product, name='add_wishlist_product'),
    path('remove_wishlist_product/<int:product_id>/', views.remove_wishlist_product, name='remove_wishlist_product'),
    path('remove_product_from_wishlist/<int:product_id>/', views.remove_product_from_wishlist, name='remove_product_from_wishlist'),
]
