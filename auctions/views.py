from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Listing, Bid, Comment


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class create_listing_form(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'url']

class bidding_form(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']

def create(request):
    if request.method == "POST":
        form = create_listing_form(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            if not listing.url:
                listing.url = "https://lijv.nl/wp-content/plugins/ninja-forms/assets/img/no-image-available-icon-6.jpg" 
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create_listing.html", {
                "form": form
            })
    else:
            return render(request, "auctions/create_listing.html", {
                "form": create_listing_form()
            })

def wishlist(request):
    return render(request, "auctions/wishlist.html")

def listing(request, TITLE):
    listing = Listing.objects.filter(title=TITLE).first()

    if request.method == "POST":
        form = bidding_form(request.POST)
        if form.is_valid():
            bidding = form.save(commit=False)
            bidding.user = request.user
            bidding.listing = request.listing
            bidding.save()
            return render(request, "auctions/listing.html")
        else:
            return render(request, "auctions/listing.html", {
            "listing" : listing,
            "form" : form
    })
    else:
        return render(request, "auctions/listing.html", {
        "listing" : listing,
        "form" : bidding_form()
    })
