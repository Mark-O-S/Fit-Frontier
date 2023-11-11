from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Wishlist
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show_wishlist(request):
    """ A view to display the user's wishlist of products """
    wishlist = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlist_products': wishlist,
    }

    return render(request, 'wish_list/wishlist.html', context)


@login_required
def add_wishlist_product(request, product_id):
    """ A function to add a product to the user's wishlist """
    product = get_object_or_404(Product, pk=product_id)
    Wishlist.objects.create(user=request.user, wishlist_product=product)

    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_wishlist_product(request, product_id):
    """ A function to remove a product from the user's wishlist on the product deatil page"""
    product = get_object_or_404(Product, pk=product_id)
    wishlist_product = Wishlist.objects.filter(user=request.user, wishlist_product=product)
    wishlist_product.delete()
    print(request)
    print(user)
    
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_product_from_wishlist(request, product_id):
    """ A function to remove a product from the user's wishlist on the wishlist page"""
    product = get_object_or_404(Product, pk=product_id)
    wishlist_product = Wishlist.objects.filter(user=request.user, wishlist_product=product)
    wishlist_product.delete()
    
    wishlist = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlist_products': wishlist,
    }

    return render(request, 'wish_list/wishlist.html', context)
