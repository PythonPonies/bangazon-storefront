from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_storefront.models import *




def display_order_and_products(request):
    """
    Method to create and display and order and all its products on the order template
    """
    customer = customer_model.Customer.objects.get(user=request.user)
    order = order_model.Order.objects.get_or_create(buyer = customer, payment_complete=0)
    order = order[0]
    products = productonorder_model.Product_On_Order.objects.filter(order_id=order.pk)
    order.products = []
    for product in products:
        order.products.extend(products_model.ProductsModel.objects.filter(pk=product.pk))
    context = {'order': order}
    return render(request, 'bangazon_storefront/order.html', context)