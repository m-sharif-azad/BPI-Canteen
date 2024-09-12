from django.db import models

# Customer Table
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)  # Optional, for delivery purposes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Menu_Item Table
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  
    category = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Order Table
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    ], default='Pending')
    payment_status = models.CharField(max_length=50, choices=[
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid')
    ], default='Unpaid')
    delivery_address = models.TextField(blank=True, null=True)  # Optional, if different from customer address

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"


# Order_Item Table
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} (Order {self.order.id})"


# Payment Table
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('Credit Card', 'Credit Card'),
        ('Cash', 'Cash'),
        ('Online Payment', 'Online Payment')
    ])
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Successful', 'Successful'),
        ('Failed', 'Failed')
    ])

    def __str__(self):
        return f"Payment {self.id} - {self.order}"


# Delivery Table
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_person = models.CharField(max_length=100)
    delivery_time = models.DateTimeField(blank=True, null=True)  # To be filled when delivery is made
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered')
    ], default='Pending')

    def __str__(self):
        return f"Delivery {self.id} - {self.order}"
