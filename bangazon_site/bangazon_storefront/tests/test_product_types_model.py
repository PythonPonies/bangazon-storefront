from bangazon_storefront.models import * 
from  django.test import TestCase
from bangazon_storefront.models.product_types_model import ProductTypes

class TestProductTypesModel(TestCase):
    """
    The purpose of this class is to test the model for categories of products on the
    bangazon site.
    Author: Ike, Main Bananas
    """

    def test_ProductTypes_model(self):
        """
        The purpose of this function is to test that categories can be added to 
        and retrieved from the database
        Author: Ike, Main Bananas
        """
        shoes = ProductTypes.objects.get_or_create(category_name="Shoes")
        what_is_zees = ProductTypes.objects.all()
        self.assertEqual( len(ProductTypes.objects.all()), 1 )

        # self.assertEqual(ProductTypes.objects.get(pk=1), shoes.pk)

    


