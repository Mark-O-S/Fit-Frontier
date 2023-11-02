from .models import Product, Category
from django.shortcuts import render, redirect, reverse, get_object_or_404


def product_review(request, product_id):
    """ A view to show an individual product review """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
