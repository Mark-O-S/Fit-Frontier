from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'rating',
        'comment',
        'reviewed_by',
        'reviewed_at',
        'headline',
        )

    ordering = ('reviewed_at',)

admin.site.register(Review, ReviewAdmin)
