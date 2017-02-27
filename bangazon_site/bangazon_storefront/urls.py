
from django.conf.urls import url, include
from django.contrib import admin
from bangazon_storefront.views import *
from bangazon_storefront.views import *

app_name = 'bangazon_storefront'
urlpatterns = [
<<<<<<< HEAD
    url(r'^$', index_view.IndexView.as_view(), name='IndexView'),
=======
    url(r'^$', index_view.IndexView.as_view(), name='index'),
>>>>>>> 0aa9c13fba8a343ea096888f68b5f168b2a913e9
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
    url(r'^order/', createorder_view.display_order_and_products, name='order'),
    url(r'^productTypes/', product_types_view.productTypes, name="productTypes"),
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
    url(r'^(?P<product_id>[0-9]+)/$', product_details_view.detail, name='product_detail'),
    url(r'^payment', paymenttype_view.PaymentTypeView.as_view(), name='PaymentTypeView'),
    url(r'^add_product_to_order', addproducttoorder_view.add_product_to_order, name='add_product_to_order'),
]

