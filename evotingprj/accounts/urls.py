from django.urls import path

from .views import *

urlpatterns = [
    path('', account_login, name='account_login'),
    path('register/', account_register, name="account_register"),
    path('logout/', account_logout, name="account_logout"),
]