from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required
from bangazon_storefront.models.product_types_model import *
from bangazon_storefront.models.products_model import *


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
        
    product_types = ProductTypes.objects.all()
    # for product_type in product_types:
    products = Product.objects.all().order_by('-id')
    context =  {'product_types' : product_types, 'products': products[:20]} 
    return render(request, 'bangazon_storefront/productTypes.html', context)

def add_product_type(request):
    """the purpose of this function is to add a product type
        author: Ike, Main Bananas
    """

    data = request.POST
    ProductTypes.objects.create(category_name=data['category_name'])
    return HttpResponseRedirect('/add/')



