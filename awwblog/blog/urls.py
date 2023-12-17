from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='home'),
    path('<slug:post>/', post_detail, name='post_detail'),
    path('comment/reply/', reply_page, name='reply'),
    path('tag/<slug:tags_slug>/',post_list, name='post_tag')
]