from django.conf.urls import url

from bangazon_storefront.views import *

app_name = 'bangazon_storefront'
urlpatterns = [
    url(r'^$', createorder_view.IndexView.as_view(), name='index'),
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
    url(r'^order/', createorder_view.OrderView.as_view(), name='order'),
    url(r'^display_order_and_products/', createorder_view.display_order_and_products, name='display_order_and_products'),
]
