from django.urls import path
from . import views


urlpatterns = [
	path('top_nav/', views.top_nav, name='top_nav'), # Top Navigation bar
    path('order/', views.order, name="order"),	 # Home page
    path('testing/', views.testing, name="testing"), # Test page
]

