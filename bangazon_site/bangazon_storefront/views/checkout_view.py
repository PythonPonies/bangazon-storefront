from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_storefront.models.paymenttype_model import PaymentType
from bangazon_storefront.models.customer_model import Customer

class CheckoutView(TemplateView):
    template_name = 'bangazon_storefront/checkout.html'

def checkout(request):
    # customer = Customer.objects.get(user=request.user)
    # payment_types = PaymentType.objects.filter(customer_id = customer)
    # customer_products = 
    # context = {'payment_types': payment_types, }

    # return render(request, 'bangazon_storefront/payment.html', context)
    pass

def confirm_payment(request):
    # payment = request.POST
    # PaymentType.objects.create(
    #     account_number = payment['account_number'],
    #     payment_name = payment['payment_name'],
    #     expiration_date = payment['expiration_date'],
    #     customer = Customer.objects.get(user=request.user),
    #     billing_address = payment['billing_address'],
    # )

    # return HttpResponseRedirect('checkout')
    pass