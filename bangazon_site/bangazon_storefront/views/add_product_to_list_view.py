from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from bangazon_storefront.models import *



# This view allows a user to add a product for sale to the generally viewable product list.
# Author: PS

	# When adding a product, users will be directed to a new template with a form for inputs:
	# Function for adding and persisting products: 
def addProduct(self, request): 
	data = request.POST
	new_product = products_model.ProductsModel.objects.create(
		title = data['title'],
		description = data['description'], 
		seller_id = data['seller_id'],
		categoryId = data['category'], 
		price = data['price'], 
		quantity = data['quantity']
	)
	print(new_product)
	return HttpResponseRedirect('/')

def renderProduct(request):
	categories = product_types_model.ProductTypes.objects.all()
	print(categories)
	return render(request, 'bangazon_storefront/add_product.html', {'categories': categories})




