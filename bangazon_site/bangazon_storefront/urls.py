
from django.conf.urls import url, include
from django.contrib import admin
from bangazon_storefront.views import product_types_view, customer_view


app_name = 'bangazon_storefront'
urlpatterns = [
    url(r'^productTypes/', product_types_view.productTypes, name="productTypes"),
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
]

