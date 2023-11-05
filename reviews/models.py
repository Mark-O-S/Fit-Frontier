from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    reviewed_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    reviewed_at = models.DateTimeField(auto_now_add=True)
    headline = models.TextField()
    testfield = models.TextField(default="test")
