from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup/', sign_up, name='signup'),
    path('ready_to_test/<int:pk>/', ready_to_test, name='ready_to_test'),
    path('test/<int:pk>/', test, name='test'),

]
