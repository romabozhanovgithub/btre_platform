from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices

def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    context = {
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "listings_text": "Listings text"
    }
    return render(request, "pages/index.html", context)

def about(request):
    realtors = Realtor.objects.order_by("-hire_date")
    m_realtors = Realtor.objects.all().filter(is_m=True)
    context = {
        "realtors": realtors,
        "m_realtors": m_realtors
    }
    return render(request, "pages/about.html", context)
