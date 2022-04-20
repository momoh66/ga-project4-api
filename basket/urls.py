from django.urls import path
from .views import *

urlpatterns = [
    path('baskets/', BasketList.as_view()),
    path('baskets/<int:pk>/', BasketRetrieveUpdateDestroy.as_view()),

]
