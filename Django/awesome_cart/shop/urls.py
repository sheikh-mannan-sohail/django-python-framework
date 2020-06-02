from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="ShopIndex"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackStatus"),
    path('search/', views.search, name="Search"),
    path('product_view/', views.prod_view, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
]
