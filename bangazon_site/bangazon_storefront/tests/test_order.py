from django.test import TestCase, Client
from django.urls import reverse
from bangazon_storefront.models import *
from bangazon_storefront.views import *


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
        # customer = customer_model.Customer(
        #     """need info from customer"""
        # )
        # customer.save()
        # self.customer = customer
        self.customer_order = order_model.Order.objects.create(
            # buyer_id=self.customer.pk,
        )
        self.client = Client()

    def test_create_an_order(self):
        """
        Test that an order can be created in the database
        """
        self.assertEqual((order_model.Order.objects.get(pk=self.customer_order.pk)).pk, self.customer_order.pk)

    def test_customer_can_create_an_order_view(self):
        """
        Test that a customer can create an order on order view
        """
        response = self.client.post('order', kwargs={'order_id': self.customer_order.pk})
        print(response)
        # self.assertTemplateUsed(response, 'order.html'
         # self.assertTrue('latest_poll_list' in resp.context)
        # self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']], [1])

       
