from django.urls import path



from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog, name='blog'),
    path('search/', search, name='search'),
    path('post/create/', post_create, name='create-post'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update', post_update, name='post-update'),
    path('post/<id>/delete', post_delete, name='post-delete'),
]