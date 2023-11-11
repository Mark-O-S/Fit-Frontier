from django.contrib import admin
from .models import Wishlist

# Register your models here.
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'wishlist_product',
        'user',
    )

    ordering = ('wishlist_product',)

admin.site.register(Wishlist, WishlistAdmin)