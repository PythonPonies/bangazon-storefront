from django.test import TestCase
from bangazon_storefront.models.products_model import *
from bangazon_storefront.models.product_types_model import *
from bangazon_storefront.models.customer_model import *

# Run `python manage.py test bangazon_storefront`
# from the root directory to run all tests

class ProductsModelTestCase(TestCase):
    """
    The ProductsModelTestCase class tests everything related to testing if products can be added to the database.

    Arguments: TestCase identifies the classes as a test class.
    Methods:   test_products_can_be_added_to_database
    Author:    Nate Baker, Main Bananas
    """

    def test_products_can_be_added_to_database(self):
        """
        test_products_can_be_added_to_database is a method to test if products can be added to the database.
        """

        # create customer
        Bill = Customer.objects.create(
            email="bill@bill.com",
            first_name="Bill",
            last_name="Bill",
            shipping_address="123 Test Way",
            phone="333-333-3333"
        )
        # pull instance of customer from databse
        bill_in_datebase = Customer.objects.get(email="bill@bill.com")
        # check that what is pushed up is what is in the database
        assertEqual(bill_in_datebase.pk, Bill.pk)

        # create new product type
        Food = ProductTypes.objects.create(label="food")
        # pull instance of product type from databse
        food_in_datebase = ProductTypes.objects.get(label="food")
        # check that what is pushed up is what is in the database
        assertEqual(food_in_datebase.pk, Food.pk)

        # create new product
        Pizza = Products.objects.create(
            title="Cheese Pizza",
            description="This is a super cheesy pizza.",
            seller_id=Bill.Customer_id,
            categoryId=Food.Food_id,
            price=9.85,
            quantity=9
        )
        # pull instance of product from databse
        pizza_in_datebase = Products.objects.get(title="Cheese Pizza")
        # check that what is pushed up is what is in the database
        assertEqual(pizza_in_datebase.pk, Pizza.pk)
