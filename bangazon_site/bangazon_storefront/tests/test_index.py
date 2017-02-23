from django.test import TestCase, Client

class TestOrder(TestCase):
    """
    This class tests everything related to the index view.

    Method List
    Arguments unittest.TestCase allows the unittest model to know what to test.
    Author Zoe LeBlanc, Python Ponies
    """
    def setUp(self):
        '''This method sets up initial instances of Client from the database'''
        self.client = Client()


    def test_index_view(self):
        """
        Test that a customer can create an order on order view
        """
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)


       
