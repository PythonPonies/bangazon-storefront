from django.views.generic.base import TemplateView
from bangazon_storefront.views.navigation_view import *

class IndexView(TemplateView):
    template_name = 'bangazon_storefront/index.html'