
from django.conf.urls import url, include
from django.contrib import admin
from bangazon_storefront.views import *
from bangazon_storefront.views import product_types_view, customer_view, paymenttype_view

app_name = 'bangazon_storefront'
urlpatterns = [
    url(r'^$', index_view.IndexView.as_view(), name='IndexView'),
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
    url(r'^productTypes/', product_types_view.productTypes, name="productTypes"),
    url(r'^productDetails/', product_details_view.productDetails, name="productDetails"),
    url(r'^payment', paymenttype_view.PaymentTypeView.as_view(), name='PaymentTypeView'),
    ]