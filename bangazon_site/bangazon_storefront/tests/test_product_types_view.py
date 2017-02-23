from django.test import TestCase
from bangazon_storefront.models.customer_model import * 
# from bangazon_storefront.models.products_model import * 
from bangazon_storefront.models.product_types_model import * 
from bangazon_storefront.views.product_types_view import * 

# Create your tests here.

class TestProductTypes(TestCase):
    """
    The purpose of this class is to test categories of products on the
    bangazon site.

    Methods: 
        setUp-
        test_get_all_product_types-
        get_all_products_for_a_given_product_type

    Author: Ike, Main Bananas
    """

    # add a category to the database
    # return all categories in the database
    # Can I get all the categories from the database?
        #self.assertContains(response, "category_name")
        #self.assertContains(response, "category_name")


    def setUp(self):
        """ The purpose of this function is to create the conditions
        necessary for my tests to be measured
        Author: Ike, Main Bananas
        """
        
        Kyrie = Customer.objects.get_or_create(User=Kyrie, phone='4257896453', shipping_address="The Flat Earth", )
        Shoes = ProductTypes.objects.get_or_create(category_name="Shoes")
        Books = ProductTypes.objects.get_or_create(category_name="Books")
        Products.objects.get_or_create("Man's Search for Meaning", "Book by Frankl",
        Kyrie.pk, Books.pk, 15.00, 3)
        Products.objects.get_or_create("The Four Agreements", "Book by Ruiz",
        Kyrie.pk, Books.pk, 16.00, 4)


    def test_get_all_product_types(self):
        response = ProductTypes.objects.filter()
        print(response, "this is the response for all product types hopefully")
        self.assertContains(response, "Shoes")
        self.assertContains(response, "Books")

    def get_all_products_for_a_given_product_type(self):

        #a product type category in the database
        #add at least two product in a particular product type category
        # a manner in which to select a specific product type category
        #a getter function for all the products in a category

        all_products = Products.objects.filter(category_name__exact="Books")
        # an assertion that the product type category contains our listed products
        self.assertContains(all_products, "Man's Search for Meaning")
        self.assertContains(all_products, "The Four Agreements")






