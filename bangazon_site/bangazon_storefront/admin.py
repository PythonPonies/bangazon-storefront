from django.contrib import admin

# Register your models here.
from bangazon_storefront.models import *
admin.site.register(customer_model.Customer)
admin.site.register(order_model.Order)