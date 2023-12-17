from django.urls import path

from .views import *
# from .user_password import export_to_csv

app_name= 'account'

urlpatterns  = [
    path('login/', account_login, name='account_login'),
    path('logout/', account_logout, name='account_logout'),
    # path('create-csv/', export_to_csv, name='admin_view'),
]