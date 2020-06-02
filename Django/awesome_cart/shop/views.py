from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "shop/index.html")


def about(request):
    return HttpResponse("About our e-cart service")


def contact(request):
    return HttpResponse("Contact our e-cart service")


def tracker(request):
    return HttpResponse("Track your order status ")


def search(request):
    return HttpResponse("Search what you need")


def prod_view(request):
    return HttpResponse("Product view ")


def checkout(request):
    return HttpResponse(" Checkout status")
