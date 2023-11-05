from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('edit_review/<int:product_id>/', views.edit_product_review, name='edit_product_review'),
    path('delete_review/<int:product_id>/', views.delete_product_review, name='delete_review'),
    path('show_review_product/<int:product_id>/', views.show_review_product, name='show_review_product'),
    path('show_edit_product_review/<int:product_id>/', views.show_edit_product_review, name='show_edit_product_review'),
]
