from django.db import models
from . import order_model


class Product_On_Order(models.Model):
    ''' 
    The Product On Order class is a model that defines a join table for Product & Order.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc, Main Bananas
    '''
    # product = models.ForeignKey(product_model.Product, null=True, related_name='products_on_order')
    order = models.ForeignKey(order_model.Order, null=True, related_name='products_on_order')

