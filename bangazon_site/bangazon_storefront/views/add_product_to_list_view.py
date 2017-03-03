from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from bangazon_storefront.models import *



# This view allows a user to add a product for sale to the generally viewable product list.
# Author: PS

	# When adding a product, users will be directed to a new template with a form for inputs:
	# Function for adding and persisting products: 
def addProduct(request): 
	data = request.POST
	print(data['category'])
	seller = customer_model.Customer.objects.get(user=request.user)
	product_type = product_types_model.ProductTypes.objects.get(category_name=data['category'])
	new_product = products_model.Product.objects.create(
		title = data['title'],
		description = data['description'], 
		seller = seller,
		product_type = product_type, 
		price = data['price'], 
		quantity = data['quantity']
	)
	return HttpResponseRedirect('/')

def renderProduct(request):
    categories = product_types_model.ProductTypes.objects.all()
    return render(request, 'bangazon_storefront/add_product.html', {'categories': categories})



