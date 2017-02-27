from bangazon_storefront.models.order_model import *
from bangazon_storefront.models.customer_model import *

class Navigation():
    """
    The Navigation class contains methods needed by the navigation bar view.

    Arguments: TestCase identifies the classes as a test class.
    Methods:   get_products_for_active_customer
    Author:    Nate Baker, Main Bananas
    """

    def get_products_for_active_customer(request):
        """
        get_products_for_active_customer is a method that returns the number of products that the active customer currently has.
        """
        if request.user.is_authenticated():
            # return number of their active products
            customer = Customer.objects.get(user=request.user)
            order = Order.objects.get_or_create(buyer=customer, payment_complete=0)
            order_number = order[0]
            products = order_number.products.all().count()
            return products
        else:
            # if user is not logged in show 0 next to cart
            return 0