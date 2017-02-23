from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_storefront.models import *


class IndexView(TemplateView):
    template_name = 'bangazon_storefront/index.html'
    

class OrderView(TemplateView):
    template_name = 'bangazon_storefront/order.html'

def create_order(request):
    data = request.POST 
    # customer = customer_model.Customer.objects.filter(user=request.user)
    # order = order_model.Order(
    #     buyer_id = customer.pk
    # )
    # order.save()

def display_order_and_products(request):
    # customer = customer_model.Customer.objects.filter(user=request.user)
    # order = order_model.Order.objects.filter(buyer_id=customer.pk, payment_complete=0)

    order.products.all() 
    context = {'order': order}
    return render(request, 'bangazon_storefront/order.html', context)