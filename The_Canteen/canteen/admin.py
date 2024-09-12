from django.contrib import admin
from .models import Customer, MenuItem, Order, OrderItem, Payment, Delivery

admin.site.register(Customer)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Delivery)
