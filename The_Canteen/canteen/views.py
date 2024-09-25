from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from .models import MenuItem, Order, OrderItem, Customer, Payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required

# MENU page (order.html)
def order(request):
    if request.method == "POST":
        delivery_fee = 2 # hardcoded fee - should be taken from database later
        total_price  = 0
        global selected_items
        global total_food_price
        global customer

        selected_items_ids = request.POST.getlist('selected_items')
        selected_items = MenuItem.objects.filter(id__in=selected_items_ids)
        total_food_price = sum(item.price for item in selected_items)
        customer = Customer.objects.get(user=request.user)

        # redirect to basket.html page and pass selected items
        return render(request, 'basket.html', {
            'selected_items': selected_items,
            'total_food_price': total_food_price,
            'customer': customer,
            'delivery_fee': delivery_fee,
            'total_price':total_price
            })
    
    menuitems = MenuItem.objects.all()
    return render(request, 'order.html', {'menuitems': menuitems})

# Shopping basket page
def basket(request):
    if request.method == 'POST':
        global selected_items
        global total_food_price
        global customer

        # Check which delivery method was selected
        delivery_method = request.POST.get('delivery_method')
        delivery_fee = 2 if delivery_method == 'delivery' else 0

        # Add delivery fee to total price if applicable
        final_total_price = total_food_price + delivery_fee

        # Send email confirmation to customer
        subject = 'Order Confirmation'
        message = f'Hi {customer.firstname}, your order has been received.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [customer.email, ]
        send_mail( subject, message, email_from, recipient_list )

        # Prepare data for the final page
        context = {
            'selected_items': selected_items,
            'total_items': len(selected_items),
            'total_price': final_total_price,
            'delivery_method': delivery_method,
            'customer': customer,
        }

        # Redirect to final.html page
        return render(request, 'final.html', context)
    
    template = loader.get_template('basket.html')
    return HttpResponse(template.render(request=request))

# Final page - order summary
def final(request):
    template = loader.get_template('final.html')
    return HttpResponse(template.render(request=request))

# Contact page
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