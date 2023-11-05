from .models import Review, Product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def add_review(request, product_id):
    """ A view to add an individual product review """
    
    if not request.user.is_authenticated:
        messages.warning(request, "Only logged in users can add a review")
        return render(request, 'home/index.html')

    product = get_object_or_404(Product, pk=product_id)
    product_reviews = Review.objects.filter(product=product)

    user_product_review = (
        [product_review for product_review in product.reviews.all()
            if request.user == product_review.reviewed_by]
    )
    user_reviewed_product = len(user_product_review) > 0

    context = {
        'product': product,
        'user_reviewed_product': user_reviewed_product,
        'product_reviews': product_reviews
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
            messages.success(request, "Your review has been created!")
            return render(request, 'products/product_detail.html', context)
    
    else:
        if user_reviewed_product:
            messages.warning(request, "You have already created a review "
                                      "for this product. You can edit your "
                                      "review instead!")
            return redirect(reverse('product_detail', args=[product_id]))

    return render(request, 'products/product_detail.html', context)


@login_required
def edit_product_review(request, product_id):
    """ A view to update an individual product review """
    if not request.user.is_authenticated:
        messages.warning(request, "Only logged in users can edit a review")
        return render(request, 'home/index.html')

    product = get_object_or_404(Product, pk=product_id)
    product_reviews = Review.objects.filter(product=product)

    user_product_review = (
        [product_review for product_review in product.reviews.all()
            if request.user == product_review.reviewed_by]
    )
    user_reviewed_product = len(user_product_review) > 0

    context = {
        'product': product,
        'user_reviewed_product': user_reviewed_product,
        'product_reviews': product_reviews
    }

    if request.method == 'POST':
        rating = request.POST.get('rating', 5)
        content = request.POST.get('content')
        headline = request.POST.get('headline')

        if content:
            user_product_review[0].rating = rating
            user_product_review[0].comment = content
            user_product_review[0].headline = headline
            user_product_review[0].save()

            messages.success(request, "Your review has been updated!")
            return render(request, 'products/product_detail.html', context)

    return render(request, 'products/product_detail.html', context)


@login_required
def delete_product_review(request, product_id):
    """ A view to delete an individual product review """
    if not request.user.is_authenticated:
        messages.warning(request, "Only logged in users can delete a review")
        return render(request, 'home/index.html')

    product = get_object_or_404(Product, pk=product_id)
    product_reviews = Review.objects.filter(product=product)

    user_product_review = (
        [product_review for product_review in product.reviews.all()
            if request.user == product_review.reviewed_by]
    )

    context = {
        'product': product,
        'user_reviewed_product': False,
        'product_reviews': product_reviews
    }

    if request.method == 'POST':
        user_product_review[0].delete()

        messages.success(request, "Your review has been deleted!")
        return render(request, 'products/product_detail.html', context)

    return render(request, 'products/product_detail.html', context)


@login_required
def show_review_product(request, product_id):
    """ A view to add an individual product review """
    product = get_object_or_404(Product, pk=product_id)

    user_product_review = (
        [product_review for product_review in product.reviews.all()
            if request.user == product_review.reviewed_by]
    )
    user_reviewed_product = len(user_product_review) > 0

    context = {
        'product': product,
    }

    if user_reviewed_product:
        messages.warning(request, "You have already created a review "
                                    "for this product. You can edit your "
                                    "review instead!")
        return redirect(reverse('product_detail', args=[product_id]))

    return render(request, 'reviews/add_product_review.html', context)


@login_required
def show_edit_product_review(request, product_id):
    """ A view to edit an individual product review """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'reviews/edit_product_review.html', context)


@login_required
def show_delete_product_review(request, product_id):
    """ A view to delete an individual product review """
    product = get_object_or_404(Product, pk=product_id)

    user_product_review = (
        [product_review for product_review in product.reviews.all()
            if request.user == product_review.reviewed_by]
    )
    user_reviewed_product = len(user_product_review) > 0

    context = {
        'product': product,
    }

    if not user_reviewed_product:
        messages.warning(request, "You have no review to delete for this product. You can create a new review!")
        return redirect(reverse('product_detail', args=[product_id]))

    return render(request, 'reviews/delete_product_review.html', context)
