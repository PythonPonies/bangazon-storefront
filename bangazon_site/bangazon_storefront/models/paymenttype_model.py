from django.db import models
from bangazon_storefront.models.customer_model import *

class PaymentType(models.Model):
    """
        PaymentType class contains pertinent data related to payment types associated with customer accounts.

        Author: Steven Holmes
    """
    account_number = models.IntegerField()
    payment_name = models.CharField(max_length=20, default='Unknown Payment Name')
    expiration_date = models.CharField(max_length=10)
    billing_address = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)