from django.views.generic.base import TemplateView
from bangazon_storefront.models.order_model import *
from bangazon_storefront.models.customer_model import *
from django.shortcuts import render

def Index(request):
    # check if user is logged index
    if request.user.is_authenticated():
        print(request.user, "is logged in")
        # return number of their active products
        # get customer
        customer = Customer.objects.get(user=request.user)
        order = Order.objects.get_or_create(buyer=customer, payment_complete=0)
        order_number = order[0]
        products = order_number.products.all().count()

    else:
        # if user is not logged in show 0 next to cart
        products = 0
    context = {'order_number': products}
    return render(request, 'bangazon_storefront/index.html', context)