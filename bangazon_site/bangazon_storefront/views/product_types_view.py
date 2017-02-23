from django.shortcuts import render
# from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required
from bangazon_storefront.models import product_types_model #,Products


# Create your views here.
def productTypes(request):
    """the purpose of this function is to render the
       page for the product categories
    """
    # productTypes = 
    return render(request, 'bangazon_storefront/productTypes.html')

# @login_required
def all_products_for_a_given_product_type(request):
    pass
    """the products for a given product type page for bangazon site"""
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # context =  {'topics' : topics} # a context is a dictionary in which
    #keys are names we'll use in the template to access the data and values are 
    #the data we need to send to the template
    # return render(request, 'learning_logs/topics.html', context)

