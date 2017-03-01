from django.db import models
from bangazon_storefront.models.product_types_model import *
from bangazon_storefront.models.customer_model import *

class Product(models.Model):
    """
    The ProductModel class creates the product table and all related fields in the database.

    Arguments: The models.Model argument lets Django know this class will be used to create a database table.
    Author:    Nate Baker, Main Bananas
    """
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    seller = models.ForeignKey(Customer, blank = True)
    product_type = models.ForeignKey(ProductTypes, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=1)