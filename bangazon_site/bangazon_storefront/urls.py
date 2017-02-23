from django.conf.urls import url

from bangazon_storefront.views import *

app_name = 'bangazon_storefront'
urlpatterns = [url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
] 