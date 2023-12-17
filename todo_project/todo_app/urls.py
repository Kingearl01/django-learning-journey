from django.urls import path
from .views import *

urlpatterns = [
    path('', ListListView.as_view())
    # path('', ListListView.as_view(), 'index')
]
