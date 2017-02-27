from django.views.generic.base import TemplateView
from bangazon_storefront.models.order_model import *
from django.shortcuts import render

def Index(request):
    # check if user is logged index
    if request.user.is_authenticated():
        print(request.user, "is logged in")
        # return number of their active products
        order_number = 33
    else:
        # if user is not logged in show 0 next to cart
        order_number = 0
    context = {'order_number': order_number}
    return render(request, 'bangazon_storefront/index.html', context)