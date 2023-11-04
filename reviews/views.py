from .models import Review, Product
from django.shortcuts import render, redirect, reverse, get_object_or_404


def add_product_review(request, product_id):
    """ A view to show an individual product review """
    print("Success")

    product = get_object_or_404(Product, pk=product_id)
    product_review = Review.objects.filter(product=product)

    context = {
        'product_review': product_review,
    }

    return render(request, 'reviews/product_review.html', context)


def list_all_reviews(request):
    """ A view to show an individual product review """
    print("Success")

    product = get_object_or_404(Product, pk=product_id)
    product_review = Review.objects.filter(product__in=product)

    context = {
        'product_review': product_review,
    }

    return render(request, 'reviews/product_review.html', context)
