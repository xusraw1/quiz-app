from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup/', sign_up, name='signup'),
    path('ready_to_test/<int:pk>/', ready_to_test, name='ready_to_test'),
    path('test/<int:pk>/', test, name='test'),
    path('checktest/<int:pk>/', chek_test, name='checktest'),
    path('new_test/', new_test, name='new_test'),
    path('new_question/<int:pk>/', new_question, name='new_question'),

]
