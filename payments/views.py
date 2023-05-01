from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest, OrdersCaptureRequest
from .secrets import client_id, client_secret

# Set up PayPal client

environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
client = PayPalHttpClient(environment)

# Create a PayPal order
def create_order():
    request = OrdersCreateRequest()
    request.prefer('return=representation')
    request.request_body({
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "amount": {
                    "currency_code": "USD",
                    "value": "100.00"
                }
            }
        ]
    })
    response = client.execute(request)
    return response.result.id

# Capture a PayPal order
def capture_order(order_id):
    request = OrdersCaptureRequest(order_id)
    request.prefer('return=representation')
    response = client.execute(request)
    return response.result.status

# View function for PayPal payment
@csrf_exempt
def payment(request):
    if request.method == "POST":
        order_id = create_order()
        return redirect("https://www.sandbox.paypal.com/checkoutnow?token=" + order_id)
    else:
        return render(request, "payment.html")

# View function for success page
def success(request):
    order_id = request.GET.get("token")
    status = capture_order(order_id)
    return render(request, "success.html", {"status": status})


