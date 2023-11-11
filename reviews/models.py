from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE, null=False, blank=False
        )
    rating = models.IntegerField(default=5, null=False, blank=False)
    comment = models.TextField(null=False, blank=True)
    reviewed_by = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE, null=False, blank=False
        )
    reviewed_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    headline = models.TextField(null=False, blank=True)
