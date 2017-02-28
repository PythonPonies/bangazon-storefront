from bangazon_storefront.models.order_model import *
from bangazon_storefront.models.customer_model import *

def navigation(request):
    """
    The Index class calls get_products_for_active_customer so that it can draw the index.html template while passing how many products the active customer has.

    Arguments: This class needs request to know which user is currently active.
    Author:    Nate Baker, Main Bananas
    """
    if request.user.is_authenticated():
            # return number of their active products
            customer = Customer.objects.get(user=request.user)
            order = Order.objects.get_or_create(buyer=customer, payment_complete=0)
            order_number = order[0]
            products = order_number.products.all().count()
            
    else:
        # if user is not logged in show 0 next to cart
        products = 0
    # products = Navigation.get_products_for_active_customer(request)
    context = {'order_number': products}
    return render(request, 'bangazon_storefront/navigation.html', context)

# class Navigation():
#     """
#     The Navigation class contains methods needed by the navigation bar view.

#     Arguments: TestCase identifies the classes as a test class.
#     Methods:   get_products_for_active_customer
#     Author:    Nate Baker, Main Bananas
#     """

#     def get_products_for_active_customer(request):
#         """
#         get_products_for_active_customer is a method that returns the number of products that the active customer currently has.
#         """
#         