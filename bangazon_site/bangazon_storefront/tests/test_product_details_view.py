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

    def test_product_detail_view_shows_product_data(self):
        """
        test_product_detail_view_shows_product_data tests if a product can be created and then displayed on a product details view.
        """

        # test creating a customer so I can create a product
        Bill = Customer.objects.create(
            email="bill@bill.com",
            first_name="Bill",
            last_name="Bill",
            shipping_address="123 Test Way",
            phone="333-333-3333"
        )
        bill_in_datebase = Customer.objects.get(email="bill@bill.com")
        assertEqual(bill_in_datebase.pk, Bill.pk)

        # test creating new product type so I can create a product
        Food = ProductTypes.objects.create(label="food")
        food_in_datebase = ProductTypes.objects.get(label="food")
        assertEqual(food_in_datebase.pk, Food.pk)

        # test creating new product
        Pizza = Products.objects.create(
            title="Cheese Pizza",
            description="This is a super cheesy pizza.",
            seller_id=Bill.Customer_id,
            categoryId=Food.Food_id,
            price=9.85,
            quantity=9
        )
        pizza_in_datebase = Products.objects.get(title="Cheese Pizza")
        assertEqual(pizza_in_datebase.pk, Pizza.pk)

        # test if the proper product details url loads successfully
        path = '/product-details/' + Pizza.pk + '/'
        request = self.client.post(path)
        self.assertEqual(request.status_code, 200)

        # test if product details appears on product details view
        request2 = self.client.get(reverse(path))
        self.assertEqual(request2.status_code, 200)
        self.assertContains(request2.content, "Cheese Pizza")