from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create-post/', CreatePostView.as_view(), name='add-post'),
    path('update-post/<slug:slug>/', UpdatePostView.as_view(), name='update-post'),
    path('delete-post/<slug:slug>/', DeletePostView.as_view(), name='delete-post'),
    path('<slug:slug>/', DetailPostView.as_view(), name='post-detail'),
    path('category/<category>', CatListView.as_view(), name='category')


]