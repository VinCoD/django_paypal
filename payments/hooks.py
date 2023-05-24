from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import receiver


@receiver(valid_ipn_received)
@csrf_exempt
def webhook(sender, **kwargs):
    ipn_obj = sender
    print('this is hook')
    return

