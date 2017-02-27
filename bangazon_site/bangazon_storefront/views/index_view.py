from django.views.generic.base import TemplateView
from bangazon_storefront.views.navigation_view import *
from django.shortcuts import render

def Index(request):
    products = Navigation.get_products_for_active_customer(request)
    context = {'order_number': products}
    return render(request, 'bangazon_storefront/index.html', context)