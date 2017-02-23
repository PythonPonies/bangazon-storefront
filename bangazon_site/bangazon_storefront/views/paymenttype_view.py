from django.views.generic.base import TemplateView
from bangazon_storefront.models.paymenttype_model import PaymentType



class PaymentTypeView(TemplateView):

    template_name = 'bangazon_storefront/payment.html'

    def get_payment_types(request, customerId):
        user_payments = PaymentType.objects.filter(userId=userId)
        return user_payments

    def add_payment_type(request, account_number, payment_name, expiration_date, billing_address, customer):
        payment = request.POST
        PaymentType.objects.create(
            account_number = payment['account_number'],
            payment_name = payment['payment_name'],
            expiration_date = payment['expiration_date'],
            billing_address = payment['billing_address'],
            customer = payment['customer']
        )

        return HttpResponseRedirect('/')

# def add_new_payment(request):
#     data = request.POST
#     Payment.objects.create_user(
#         username = data['username'],
#         email = data['email'],
#         password = data['password'],
#         first_name = data['first_name'],
#         last_name = data['last_name']
#     )
    
#     return login_user(request)







