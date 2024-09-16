from django.urls import path
from . import views


urlpatterns = [
    path('order/', views.order, name="order"),	 # Home page
    path('testing/', views.testing, name="testing"), # Test page
    path('contact/', views.contact, name="contact"), # Contact page
    path('basket/', views.basket, name="basket"), # Shopping Basket page
]

