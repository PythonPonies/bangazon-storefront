from django.test import TestCase
from bangazon_storefront.models.customer_model import *
from django.contrib.auth.models import User
from bangazon_storefront.views.customer_view import * 


# If login/registration redirect to the desired page, these features are functional:
class TestCustomerView(TestCase):

	def test_login_redirects_to_desired_page(self):		
		response = self.client.get(reverse('bangazon_storefront:login'))
		self.assertTemplateUsed('/productTypes/')
		self.assertEqual(response.status_code, 200)

	def test_register_redirects_to_desired_page(self):		
		response = self.client.get(reverse('bangazon_storefront:register'))
		self.assertTemplateUsed('/login/')
		self.assertEqual(response.status_code, 200)









