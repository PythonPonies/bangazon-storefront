from django.shortcuts import get_object_or_404, render
from bangazon_storefront.models import *

def index(request):
    """"""
    producttypes = product_types_model.ProductTypes.objects.all()    
    products = []
    for p_type in producttypes:
        p = product_types_model.ProductTypes.objects.get(id=p_type.id).product_set.all().order_by('-id')[:5]
        products.extend(p.values())
    
    return render(request, 'bangazon_storefront/index.html', {'producttypes': producttypes, 'products': products})
