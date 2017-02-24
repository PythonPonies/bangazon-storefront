from django.db import models
from . import customer_model, products_model, paymenttype_model


class Order(models.Model):
    ''' The Order class is a model that defines which data is available in the Order table so a database can be created from it.

    Method List:
        -none

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc, Main Bananas
    '''
    date_created = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(customer_model.Customer, null=True, on_delete=models.CASCADE, related_name='orders')
    payment_type = models.ForeignKey(paymenttype_model.PaymentType, blank=True, null=True, on_delete=models.CASCADE)
    payment_complete = models.BooleanField(default=False)