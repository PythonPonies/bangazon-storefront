from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_storefront.models import *
import requests, json

def detail(request, product_id):
    """This method generates the information about the product on the detail page."""

    product = get_object_or_404(products_model.Product, pk=product_id)
    print(product.title)
    r=requests.get("https://pixabay.com/api/?key=3448017-bb600a501ab86925a33197f5b&q="+product.title+"&image_type=photo").json();
    image = r['hits'][0]
    image = image['webformatURL']
    return render(request, 'bangazon_storefront/product_detail.html', {'product': product, 'image': image})
    