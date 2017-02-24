from django.test import TestCase
from bangazon_storefront.views.navigation_view import *

# Run `python manage.py test bangazon_storefront`
# from the root directory to run all tests

class NavigationViewTestCase(TestCase):
    """
    The NavigationViewTestCase class tests everything related to data appearing in the navigation bar

    Arguments: TestCase identifies the classes as a test class.
    Methods:   test_navigation_bar_knows_number_of_products_on_order
    Author:    Nate Baker, Main Bananas
    """

    def test_navigation_bar_knows_number_of_products_on_order(self):
        """
        test_navigation_bar_knows_number_of_products_on_order is a method to test if the navigation bar has a method that returns the number of products on an order for the active user.
        """

        number_of_products = Navigation.get_products_for_active_customer()
        it_is_a_number = isinstance(number_of_products, int)
        self.assertTrue(it_is_a_number)