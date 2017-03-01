from django.shortcuts import get_object_or_404, render
from bangazon_storefront.models import *
def home(request):
    producttypes = product_types_model.ProductTypes.objects.all()
    products = products_model.Product.objects.all().order_by('-id')
    return render(request, 'bangazon_storefront/home.html', {'producttypes': producttypes, 'products': products[:5]})   
