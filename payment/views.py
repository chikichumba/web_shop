from django.shortcuts import render
import stripe
import requests
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from orders.models import Order
from cart.views import CartMixin
from decimal import Decimal
import json
import hashlib
import base64

# stripe login
# stripe listen --forward-to localhost:8000/payment/stripe/webhook/

