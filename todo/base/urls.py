from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),

    path('', TaskListView.as_view(), name='tasks'),
    path('task-details/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('create-task/', TaskCreateView.as_view(), name='create_task'),
    path('update-task/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('delete-task/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
]
