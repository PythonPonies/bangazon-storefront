from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_storefront.models.paymenttype_model import PaymentType
from bangazon_storefront.models.customer_model import Customer
from bangazon_storefront.models.order_model import Order

# class CheckoutView(TemplateView):
    # template_name = 'bangazon_storefront/checkout.html'

def checkout(request):
    customer = Customer.objects.get(user=request.user)
    payment_types = PaymentType.objects.filter(customer_id = customer)
    order = Order.objects.get(buyer_id = customer)
    context = {'payment_types': payment_types}

    return render(request, 'bangazon_storefront/checkout.html', context)

def confirm_payment(request):

    pass