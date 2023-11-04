from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_reviews, name='list_all_reviews'),
    path('add_product_review/<int:product_id>/', views.add_product_review, name='add_product_review'),
]
