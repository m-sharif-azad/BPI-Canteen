# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from canteen.models import Customer

from .models import *

# Define a view function for the home page
def home(request):
	return render(request, 'home.html')

# Define a view function for the login page
def login_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			messages.error(request, 'Invalid Username')
			return redirect('/login/')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "Invalid Password")
			return redirect('/login/')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			return redirect('/home/')
	
	# Render the login page template (GET request)
	return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		phone_number = request.POST.get('phone')
		address = request.POST.get('address')
		zipcode = request.POST.get('zipcode')
		city = request.POST.get('city')
		country = request.POST.get('country')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		# Create a new User object with the provided information
		user = Customer.objects.create(
			firstname=firstname,
			lastname=lastname,
			email=email,
			phone_number=phone_number,
			address=address,
			zipcode=zipcode,
			city=city,
			country=country,
		)
		user.save()
		
		user = User.objects.create_user(
			first_name=firstname,
			last_name=lastname,
			email=email,
			username=username,
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('/register/')
	
	# Render the registration page template (GET request)
	return render(request, 'register.html')
