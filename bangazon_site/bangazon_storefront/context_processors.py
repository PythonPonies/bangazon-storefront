from bangazon_storefront.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def navigation(context):
    """
    The Index class calls get_products_for_active_customer so that it can draw the index.html template while passing how many products the active customer has.

    Arguments: This class needs request to know which user is currently active.
    Author:    Nate Baker, Main Bananas
    """
    if context.user.is_authenticated():
            # return number of their active products
            customer = customer_model.Customer.objects.get_or_create(user=context.user)
            order = order_model.Order.objects.get_or_create(buyer=customer[0], payment_complete=0)
            order_number = order[0]
            products = order_number.products.all().count()
            welcome_message = 'Welcome '+customer[0].user.first_name + ' ' + customer[0].user.last_name
            list_of_nav = [ 
                {
                    'name':'Product Types',
                    'link': '/productTypes/',
                    'prop': 'left'
                },
                {
                    'name':'Sell Product',
                    'link': '/add/',
                    'prop': 'left'
                },
                {
                    'name': 'View Cart',
                    'link': '/order/',
                    'number': products,
                    'prop': 'right'
                },
                {
                    'name':'Logout',
                    'link': '/logout/',
                    'prop': 'right'
                },
                {
                    'name': welcome_message,
                    'link': '#',
                    'prop': 'right'
                }
            ]
    else:
        # if user is not logged in show 0 next to cart
        list_of_nav = [
                {
                    'name':'View Products',
                    'link': '/productTypes/'
                },
                {
                    'name':'Login',
                    'link': '/login/'
                }
            ]
    # products = Navigation.get_products_for_active_customer(request)
    return {'navigation': list_of_nav}
    