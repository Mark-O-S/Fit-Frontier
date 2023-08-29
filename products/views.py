from django.shortcuts import render
from .models import Product

# Create your views here.


def store(request):
    """ A view to show all products in the store """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/store.html', context)
