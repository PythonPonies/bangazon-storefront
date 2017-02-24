from django.test import TestCase
# from bangazon_storefront.models.paymenttype_model import *
# from bangazon_storefront.views.paymenttype_view import *

class CompleteOrderViewsTests(TestCase):
    """
        This class tests aspects of the CompleteOrder view methods in relation to the customer's ability to complete a given order. 

        Methods:
            test_user_can_select_payment_type_for_order - Tests user's ability to add a new payment type to be associated with their account and to use for order completion.
            test_user_can_confirm_order_completion - Tests user's ability to view existing payment types upon request. The application should return their payment types from the database and display them to the customer user. 

        Author: Steven Holmes (Main Bananas)
    """

    def test_user_can_select_payment_type_for_order(self):
        pass
        # available_payment_types = PaymentTypeView.get_payment_types()
        # chosen_payment_type = available_payment_types[0]
        # make an assertion. but WHAT assertion should be made?

    def test_user_can_confirm_order_completion(self):
        pass

