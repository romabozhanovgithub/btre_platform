from django.contrib import admin
from .models import Listing, ListingImage

class ListingImageAdmin(admin.StackedInline):
    model = ListingImage

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageAdmin]

    list_display = ("id", "title", "is_published", "price", "list_date", "realtor")
    list_display_links = ("id", "title")
    list_filter = ("realtor",)
    list_editable = ("is_published",)
    search_fields = ("title", "id")
    list_per_page = 25

    class Meta:
        model = Listing

"""
@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    pass
"""
