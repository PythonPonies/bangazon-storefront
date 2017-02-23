from django.db import models

class ProductsModel(models.Model):
    """
    The ProductModel class creates the product table and all related fields in the database.

    Arguments: The models.Model argument lets Django know this class will be used to create a database table.
    Author:    Nate Baker, Main Bananas
    """
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    seller_id = models.ForeignKey(Customer)
    categoryId = models.ForeignKey(ProductTypes)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=1)