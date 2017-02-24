from django.test import TestCase
from bangazon_storefront.models.products_model import *
from bangazon_storefront.models.product_types_model import *
from bangazon_storefront.models.customer_model import *
from bangazon_storefront.views.product_details_view import *

# Run `python manage.py test bangazon_storefront`
# from the root directory to run all tests

class ProductDetailsTestCase(TestCase):
    """
    The ProductDetailsTestCase class tests everything related to testing if the Product Details View is working.

    Arguments: TestCase identifies the classes as a test class.
    Methods:   test_product_detail_view_shows_product_data
    Author:    Nate Baker, Main Bananas
    """
    def setUp(self):
        '''This method sets up initial instances of Customer from the database'''
        user = User.objects.create_user(
            first_name = "Zoe",
            last_name = "LeBlanc",
            username = "zoe",
            email = "z@z.com",
            password = "1234asdf"
        )
        self.customer = customer_model.Customer.objects.create(
            user = user,
            phone = "513498234",
            shipping_address="asdfasf"
        )
        product_type = product_types_model.ProductTypes.objects.create(category_name="Test")
        self.product = products_model.ProductsModel.objects.create(
            title="Cheese Pizza",
            description="This is a super cheesy pizza.",
            seller_id=self.customer,
            categoryId=product_type,
            price=9.85,
            quantity=9
        )
        self.client.login(
            username = "zoe",
            password = "1234asdf"
        )

    def test_product_detail_view_shows_product_data(self):
        """
        test_product_detail_view_shows_product_data tests if a product can be created and then displayed on a product details view.
        """
        # response = self.client.get(reverse('bangazon_storefront:detail', kwards={'rp=}))
        pass