from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_storefront.models.customer_model import *

# Work in Progress--will include login/register views
# Author PS

class CustomerView(TemplateView):
	template = "templates/customer_view"