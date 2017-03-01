from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from bangazon_storefront.models.products_model import *
from bangazon_storefront.models.categories import *
from bangazon_storefront.models.product_types import * 


class AddProductsTest(TestCase):

	def test_user_can_add_products(self):
		
		BillyBob = User.objects.create_user(
					username="BillyBob",
					last_name ="Billerton",
					)
				# inject user into customer
				self.BillyBob = Customer.objects.create(
					user=BillyBob,
					phone = "333-333-4444",
					shipping_address="123 Bill Way",
					# date_account_created="2017-02-22",
					)
		food = ProductTypes.objects.get_or_create(category_name="food")

	def test_login_redirects_to_desired_page(self):		
		response = self.client.get(reverse('bangazon_storefront:add'))
		self.assertTemplateUsed('/')
		self.assertEqual(response.status_code, 200)


