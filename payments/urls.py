from django.urls import path, include
from .views import product_purchase

from . import views
urlpatterns = [
    path('purchase/<int:product_id>/', product_purchase, name='product_purchase'),
    path('successful', views.successful, name='successful'),
    path('cancelled', views.cancelled, name='cancelled'),
    path('paypal/', include('paypal.standard.ipn.urls')),
]