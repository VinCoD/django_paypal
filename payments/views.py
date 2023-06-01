from django.shortcuts import render

# Create your views here.


from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
import random

def payment(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "bizkwargdevsdev@gmail.com",
        "amount": "1.00",
        "item_name": "name of the item",
        "invoice": random.randint(1000, 9999),
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('successful')),
        "cancel_return": request.build_absolute_uri(reverse('cancelled')),
        
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)



def successful(request):
    return render(request, "successful.html")

def cancelled(request):
    return render(request, "cancelled.html")