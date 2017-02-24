from django.shortcuts import render
# from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required
from bangazon_storefront.models.product_types_model import *


# Create your views here.
def productTypes(request):
    """the purpose of this function is to render the
       page for the product categories

       parameters: request- The request is the HTTP request object that contains
       metadata about the request for loading into the view. Each view is
       responsible for returning an HttpResponse object.

    # a context is a dictionary in which
    # keys are names we'll use in the template to access the data and values are 
    # the data we need to send to the template
    """
        
    product_types = ProductTypes.objects.filter()
    print(productTypes, "this is product_types in the view line 22.")
    context =  {'product_types' : product_types} 
    return render(request, 'bangazon_storefront/productTypes.html', context)

# @login_required
def all_products_for_a_given_product_type(request, productType):
    pass
    """
    the purpose of this function is to return a view of products for a 
    given product type page for bangazon site
    Author: Ike, Main Bananas
    parameters: request

    """

    productType = productTypes.objects.filter(owner=request.user)
    context =  {'productTypes' : productTypes, 'products': products } # a context is a dictionary in which
    #keys are names we'll use in the template to access the data and values are 
    #the data we need to send to the template
    # return render(request, 'bangazon_storefront/allProducts.html', context)

