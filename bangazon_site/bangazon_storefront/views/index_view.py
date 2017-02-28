from bangazon_storefront.views.navigation_view import *
from django.shortcuts import render

def Index(request):
    """
    The Index class calls get_products_for_active_customer so that it can draw the index.html template while passing how many products the active customer has.

    Arguments: This class needs request to know which user is currently active.
    Author:    Nate Baker, Main Bananas
    """
    products = Navigation.get_products_for_active_customer(request)
    context = {'order_number': products}
    return render(request, 'bangazon_storefront/index.html', context)