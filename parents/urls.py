from django.urls import path
from .views import *

urlpatterns = [
    path('parents/', ParentList.as_view()),
    path('parents/detail/<int:pk>/', ParentWithStudentView.as_view()),
    path('parents/<int:pk>/', ParentRetrieveUpdateDestroy.as_view()),

]
