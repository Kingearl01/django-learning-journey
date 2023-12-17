from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=('login')), name='logout'),


    path('', IndexPage.as_view(), name='home'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('update/<int:pk>', UpdateTask.as_view(), name='update'),
    path('create/', CreateTask.as_view(), name='create'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete'),
]