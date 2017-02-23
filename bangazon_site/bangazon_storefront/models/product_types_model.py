from django.db import models
class ProductTypes(models.Model):
    """ 
    ProductTypes model class
    The purpose of this class is to define categories of products or product types
    author: Ike
    subclasses: Meta (ordering by name)
    
    """
    category_name = models.CharField(max_length=55)

    class Meta:
        ordering = ('category_name',)

    def __str__(self):
        return '{}'.format(self.name)