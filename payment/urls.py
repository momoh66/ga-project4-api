from django.urls import path
from .views import *

urlpatterns = [
   
    path('stripe-payments/', StripeCheckoutView.as_view()),
]
