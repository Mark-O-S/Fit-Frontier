from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'headline',
        'rating',
        'comment',
        'reviewed_by',
        'reviewed_at',
    )

    ordering = ('reviewed_at',)

admin.site.register(Review, ReviewAdmin)
