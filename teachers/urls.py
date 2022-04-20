from django.urls import path
from .views import *

urlpatterns = [
    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroy.as_view()),

]
