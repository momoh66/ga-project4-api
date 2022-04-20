from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/detail/<int:pk>/', StudentWithBasketView.as_view()),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),
    
]
