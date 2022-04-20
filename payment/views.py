from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import redirect
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY



class StripeCheckoutView(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1Kpqd0CWyX5zrgAXrnYlOiyr',
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card', ],
                mode='payment',
                success_url=settings.SITE_URL + '?success=true&={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '?canceled=true',
            )
            return redirect(checkout_session.url)
        
        except: 
            return Response({'error': 'Something went wrong when creating Stripe checkout session.'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


