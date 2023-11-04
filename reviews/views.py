from .models import Review, Product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


def add_review(request, product_id):
    """ A view to add an individual product review """
    product = get_object_or_404(Product, pk=product_id)

    context = {
            'product': product,
        }

    if request.method == 'POST':
        rating = request.POST.get('rating', 5)
        content = request.POST.get('content')
        headline = request.POST.get('headline')

        if content:
            Review.objects.create(
                product=product,
                rating = rating,
                comment=content,
                headline =headline,
                reviewed_by=request.user,
            )
            messages.success(request, "Your review has been "
                                      "submitted!")
            return render(request, 'products/product_detail.html', context)
    
    return render(request, 'products/product_detail.html', context)


def show_review_product(request, product_id):
    """ A view to add an individual product review """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'reviews/product_review.html', context)
