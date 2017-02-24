
from django.conf.urls import url, include
from django.contrib import admin
from bangazon_storefront.views import product_types_view, customer_view, paymenttype_view


app_name = 'bangazon_storefront'
urlpatterns = [
<<<<<<< HEAD
    url(r'^$', index_view.IndexView.as_view(), name='index'),
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
    # url(r'^order/', createorder_view.OrderView.as_view(), name='order'),
    url(r'^order/', createorder_view.display_order_and_products, name='order'),
]
=======
    url(r'^productTypes/', product_types_view.productTypes, name="productTypes"),
    url(r'^customer', customer_view.CustomerView.as_view(), name='CustomerView'),
    url(r'^payment', paymenttype_view.PaymentTypeView.as_view(), name='PaymentTypeView'),
]

>>>>>>> b8bb7f0cb405983a27094c0ffcbc3e91d5191560
