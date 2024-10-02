from django.shortcuts import render
from django.http import HttpResponse
from .models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})

def about(request):
    return render(request, "listings/about.html")

def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing.html", {"listings": listings})

def contact(request):
    return render (request, "listings/contact.html")

def base(request):
    return render(request, "listings/base.html")
