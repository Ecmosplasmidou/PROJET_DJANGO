from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from .models import Band, Listing
from listing.forms import ContactUsForm, BandForm, ListingForm
from django.contrib import messages


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    return render(request, "listings/band_detail.html", {"band": band})

def band_add(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            messages.success(request, 'Le groupe a bien été enregistré.')
            return redirect('band_detail', band.id)
    else:
        form = BandForm()
    return render(request, "listings/band_add.html", {"form": form})

def band_edit(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            messages.success(request, 'Le groupe a bien été modifié.')
            return redirect('band_detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, "listings/band_edit.html", {"form": form, "band": band})

def band_delete(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    if request.method == 'POST':
        band.delete()
        messages.success(request, 'Le groupe a bien été supprimé.')
        return redirect('band_list')
    return render(request, "listings/band_delete.html", {"band": band})

def about(request):
    return render(request, "listings/about.html")

def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/object.html", {"listings": listings})

def listings_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, "listings/object_detail.html", {"listing": listing})

def listings_add(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            messages.success(request, 'L\'annonce a bien été enregistrée.')
            return redirect('listings_detail', id=listing.id)
    else:
        form = ListingForm()
    return render(request, "listings/object_add.html", {"form": form})

def listings_edit(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            listing = form.save()
            messages.success(request, 'L\'annonce a bien été modifiée.')
            return redirect('listings_detail', id=listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, "listings/object_edit.html", {"form": form, "listing": listing})

def listings_delete(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'L\'annonce a bien été supprimée.')
        return redirect("listings")
    return render(request, "listings/object_delete.html", {"listing": listing})

def email_sent(request):
    return render(request, "listings/email_sent.html")

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            send_mail(subject=f"Message from {form.cleaned_data['nom'] or 'anonyme'} via MerchEx Contact Form Us Page",
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['ecmosdev@gmail.com'],)
        return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render (request, "listings/contact.html", {"form": form})

def base(request):
    return render(request, "listings/base.html")

