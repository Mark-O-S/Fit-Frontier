from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Wishlist(models.Model):
    wishlist_product = models.ForeignKey(
        Product, related_name='wishlist', on_delete=models.CASCADE
        )
    user = models.ForeignKey(
        User, related_name='wishlist', on_delete=models.CASCADE
        )