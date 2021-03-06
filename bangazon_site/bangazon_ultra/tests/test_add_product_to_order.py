from django.test import TestCase
from django.urls import reverse
from bangazon_ultra.models import *
from bangazon_ultra.views import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class TestOrder(TestCase):
    """
    This class tests everything related to an order.

    Method List
    test_customer_can_create_an_order
    Arguments unittest.TestCase allows the unittest model to know what to test.
    Author Zoe LeBlanc, Python Ponies
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
        self.product = products_model.Product.objects.create(
            title="Cheese Pizza",
            description="This is a super cheesy pizza.",
            seller=self.customer,
            product_type=product_type,
            price=9.85,
            quantity=9
        )
        self.client.login(
            username = "zoe",
            password = "1234asdf"
        )

    def test_product_can_be_added_to_order(self):
        """
        test that a product can be added to an order
        """
        response = self.client.get(reverse('bangazon_ultra:product_detail', args={self.product.pk}))
        print(response.context['product'])
        self.assertEqual(response.status_code, 200)
        