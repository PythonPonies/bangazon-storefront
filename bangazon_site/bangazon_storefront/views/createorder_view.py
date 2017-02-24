from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_storefront.models import *


# def create_order(request):
#     data = request.POST 
#     customer = customer_model.Customer.objects.filter(user=request.user)
#     order = order_model.Order.objects.create(
#         buyer = customer.pk
#     )
#     return display_order_and_products(request)

def display_order_and_products(request):
    """
    Method to create and display and order and all its products on the order template
    """
    customer = customer_model.Customer.objects.get(user=request.user)
    order = order_model.Order.objects.get(buyer = customer)
    if order == None:
        order = order_model.Order.objects.create(
        buyer = customer
        )
    # order = order_model.Order.objects.filter(buyer=customer.pk, payment_complete=0)
    # order.products.all() 
    context = {'order': order}
    print(context)
    return render(request, 'bangazon_storefront/order.html', context)