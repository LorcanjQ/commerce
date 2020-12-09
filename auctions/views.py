from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required


from .models import User,Listing

auction_list = []


def index(request):

    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
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

@login_required
def create(request):

    if request.method == "POST":
        listing = Listing()
        listing.seller = request.user
        listing.title = request.POST["title"]
        listing.descrip = request.POST["descrip"]
        listing.start_bid = request.POST["start_bid"]
        listing.category = request.POST["category"]
        listing.image = request.POST["image"]
        listing.date = datetime.today().strftime('%Y-%m-%d %H:%M')
        listing.save()


        return render(request, "auctions/listing.html", {
            "listing" : listing

            })
    else:
        return render(request, "auctions/create.html")

def listing(request,i_d):
    return HttpResponse(i_d)
    #render(request, "auctions/listing.html", {
    #    "listing" : listing[i_d]

    #    })
