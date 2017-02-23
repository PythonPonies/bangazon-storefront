from django.test import TestCase
from bangazon_storefront.models.paymenttype_model import *
from bangazon_storefront.models.customer_model import *
from bangazon_storefront.views.paymenttype_view import *
from django.contrib.auth.models import User

class PaymentTypeViewTest(TestCase):
    """
        This class tests all aspects of PaymentTypes in relation to the customer, the database, and interactions with the Bangazon storefront interface. 

        Methods:
            test_paymenttype_view - 
            test_user_can_add_new_payment_type - Tests user's ability to add a new payment type to be associated with their account and to use for order completion.
            test_user_can_view_existing_payment_types - Tests user's ability to view existing payment types upon request. The application should return their payment types from the database and display them to the customer user. 

        Author: Steven Holmes (Main Bananas)
    """
    def test_paymenttype_view(self):
        resp = self.client.get('/payment/')
        self.assertEqual(resp.status_code, 200)

    def test_user_can_add_new_payment_type(self):

        user = User.objects.create_user(
                username = 'test_user',
                first_name = 'Testy',
                last_name = 'Testerson',
                email = 'testy@test.com'
                )

        self.customer = Customer.objects.create(
                user = user,
                phone = "123-456-7890", 
                shipping_address="123 Testing Way", 
                date_account_created="2017-12-25"
                )

        payment = PaymentType.objects.create(
                account_number = 1234567890, 
                payment_name = 'Visa', 
                expiration_date = '12-12-17', 
                billing_address = '123 Test Way', 
                customer = self.customer
                )

        print(payment.customer.id)

        saved_payment = PaymentType.objects.get(id = 1)

        self.assertEqual(saved_payment, payment)

    # def test_user_can_view_existing_payment_types(self):
    #     payment_types = PaymentTypeView.get_payment_types()
    #     self.assertIsNotNone(payment_types)


