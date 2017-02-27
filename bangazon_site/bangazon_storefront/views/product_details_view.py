from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_storefront.models import *

def detail(request, product_id):
    """This method generates the information about the product on the detail page."""
    product = get_object_or_404(products_model.ProductsModel, pk=product_id)
    return render(request, 'bangazon_storefront/product_detail.html', {'product': product})
    