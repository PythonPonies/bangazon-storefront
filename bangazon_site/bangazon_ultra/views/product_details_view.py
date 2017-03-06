from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_ultra.models import *
import requests, json

def detail(request, product_id):
    """
    The detail view maps the url product-detail.html to the data that it needs.

    Arguments: request allows Django to see user session data, product_id is used to generate the individual product
    Uncomment the lines to add pictures for each product
    Author: Zoe, Main Bananas
    """

    product = get_object_or_404(products_model.Product, pk=product_id)
    # r=requests.get("https://pixabay.com/api/?key=3448017-bb600a501ab86925a33197f5b&q="+product.title+"&image_type=photo").json();
    # image = r['hits'][0]
    # image = image['webformatURL']
    #Add image:image to render for images
    return render(request, 'bangazon_ultra/product_detail.html', {'product': product})
    