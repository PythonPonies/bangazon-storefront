from django.conf.urls import url, include
from django.contrib import admin
from bangazon_storefront.views import product_types_view


app_name = 'bangazon_storefront'
urlpatterns = [
    url(r'^productTypes/', product_types_view.productTypes, name="productTypes"),
]

