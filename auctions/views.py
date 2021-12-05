from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxInput, TextInput
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib import messages

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
        fields = ['title', 'description', 'prize', 'url']
        labels = {
            "url": "Image URL (optional):"
        }
        widgets= { 
            'title': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'prize': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.Textarea(attrs={'class': 'form-control'})
            }

class bidding_form(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']
        labels = {
            "comment_content": "Write a comment:"
        }

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

def listing(request, TITLE):
    listing = Listing.objects.filter(title=TITLE).first()
    comments = Comment.objects.filter(listing=listing)
    bids = Bid.objects.filter(listing=listing)
    highest_bid = Bid.objects.filter(listing=listing).first()

    if request.method == "POST":
        if 'bidding' in request.POST:
            form = bidding_form(request.POST)
            if form.is_valid():
                if float(request.POST['bid']) > listing.prize:
                    bidding = form.save(commit=False)
                    bidding.user = request.user
                    bidding.listing = listing
                    bidding.save()
                    listing.prize = float(request.POST['bid'])
                    listing.save()
                    messages.success(request, 'Bid successfully placed!')
                    return HttpResponseRedirect(reverse("listing", args=[TITLE]))
                else:
                    messages.warning(request, 'Your bid is not high enough...')
                    return HttpResponseRedirect(reverse("listing", args=[TITLE]))
            else:
                return render(request, "auctions/listing.html", {
                    "listing" : listing,
                    "bid_form" : form
                })
        elif 'comment' in request.POST:
            form = comment_form(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.listing = listing
                comment.save()
                return HttpResponseRedirect(reverse("listing", args=[TITLE]))
            else:
                return render(request, "auctions/listing.html", {
                    "comment_form" : form
                })
        elif 'close_listing' in request.POST:
            listing.active = False
            listing.save()
            return HttpResponseRedirect(reverse("listing", args=[TITLE]))
        return HttpResponseRedirect(reverse("listing", args=[TITLE]))

    else:
        return render(request, "auctions/listing.html", {
        "listing" : listing,
        "comments" : comments,
        "bids" : bids,
        "highest_bid" : highest_bid,
        "bid_form" : bidding_form(),
        "comment_form" : comment_form()
    })
