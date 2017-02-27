from django.conf.urls import url, include
from django.contrib import admin
from bangazon_storefront.views import *

app_name = 'bangazon_storefront'
urlpatterns = [
    url(r'^$', index_view.Index, name='index'),
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
    url(r'^order/', createorder_view.display_order_and_products, name='order'),
    url(r'^productTypes/', product_types_view.productTypes, name="productTypes"),
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
    url(r'^(?P<product_id>[0-9]+)/$', product_details_view.detail, name='product_detail'),
    url(r'^payment', paymenttype_view.get_payment_types, name='PaymentTypeView'),
    url(r'^add_payment_type', paymenttype_view.add_payment_type, name='add_payment_type'),
    url(r'^add_product_to_order', addproducttoorder_view.add_product_to_order, name='add_product_to_order'),
    url(r'^register/', customer_view.RegisterView.as_view(), name='register'),
	url(r'^register_customer/', customer_view.register_customer, name='register_customer'),
	url(r'^login/', customer_view.LoginView.as_view(), name='login'),
	url(r'^login_customer/', customer_view.login_customer, name='login_customer'),
]

