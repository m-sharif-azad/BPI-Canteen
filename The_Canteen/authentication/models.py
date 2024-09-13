from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255,null=True)
    zipcode = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    
