from django.shortcuts import render
# from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required
from bangazon_storefront.models.product_types_model import *
from bangazon_storefront.models.products_model import *

def all_products(request, productTypes_id):
    all_products = ProductsModel.objects.filter(categoryId=productTypes_id)
    product_type_name = ProductTypes.objects.get(categoryId=productTypes_id)
    print(all_products, "these are products in the all_products_view line 10")
    context =  {'products' : all_products, "productTypes_id": productTypes_id} 
    return render(request, 'bangazon_storefront/all_products.html', context)

