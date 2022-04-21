from django.urls import path
from .views import *

urlpatterns = [
   
    path('v1/payment_intents', StripeListView.as_view()),
    path('stripe-payments/<pk>', StripeCheckoutView.as_view()),

]
