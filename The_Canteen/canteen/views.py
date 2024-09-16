from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from .models import MenuItem, Order, OrderItem, Customer, Payment


# Create your views here.

# order page
def order(request):
    if request.method == "POST":
        selected_items_ids = request.POST.getlist('selected_items')
        selected_items = MenuItem.objects.filter(id__in=selected_items_ids)
        
        # Redirect to basket.html page and pass selected items
        return render(request, 'basket.html', {'selected_items': selected_items})
    
    # Fetch your menu items from the database
    menuitems = MenuItem.objects.all()
    return render(request, 'order.html', {'menuitems': menuitems})

# shopping basket page
def basket(request):
    template = loader.get_template('basket.html')
    return HttpResponse(template.render(request=request))

# contact page
def contact(request):
    template = loader.get_template('contact.html')
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        subject = f'Message from Cycling Club, user: {name}'
        message = f'{name} ({email}) wrote:\n\n{message_content}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['peter.wirth@gmail.com']

        # Send the email
        send_mail(subject, message, email_from, recipient_list)

        # Success message
        context['success_message'] = "Thank you! Your message has been sent successfully."

    return HttpResponse(template.render(context, request))

# test page
def testing(request):
    template = loader.get_template('testing.html')
    return HttpResponse(template.render(request=request))