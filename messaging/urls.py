from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', MessagesList.as_view()),
    path('messages/<int:pk>/', MessagesRetrieveUpdateDestroy.as_view()),

]
