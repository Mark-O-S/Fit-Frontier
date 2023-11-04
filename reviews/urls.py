from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('show_review_product/<int:product_id>/', views.show_review_product, name='show_review_product'),
]
