from django.urls import path

from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('software/<int:pk>', SoftwareDetailView.as_view(), name='software_detail')
]