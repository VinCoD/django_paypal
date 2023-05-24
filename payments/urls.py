from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.payment, name='payment'),
    path('successful', views.successful, name='successful'),
    path('cancelled', views.cancelled, name='cancelled'),
    path('paypal/', include('paypal.standard.ipn.urls')),
]