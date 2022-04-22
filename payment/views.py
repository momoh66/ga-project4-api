from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from basket.models import Basket
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
# from .models import Payment
from .serializers import *
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kw):
        return Response(stripe.PaymentIntent.list(limit=10))


class StripeCheckoutView(APIView):
    
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        print(f'SELF:{self}, REQUEST: {request}, ARGS:{args}, KWARGS:{kwargs}')
        basket_id=self.kwargs['pk']
        basket=Basket.objects.get(pk = basket_id)
        try:
            checkout_session=stripe.checkout.Session.create(
                line_items = [
                    {
                        'price_data': {
                            'currency': 'gbp',
                            'unit_amount': basket.amount,
                            'product_data': {
                                'name': basket.name,
                            },
                        },
                        'quantity': 1,
                    },
                ],
                payment_method_types = ['card', ],
                mode = 'payment',
                success_url = settings.SITE_URL +
                '?success=true&={CHECKOUT_SESSION_ID}',
                cancel_url = settings.SITE_URL + '?canceled=true',
            )
            return redirect(checkout_session.url)

        except:
            return Response({'error': 'Something went wrong when creating Stripe checkout session.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
