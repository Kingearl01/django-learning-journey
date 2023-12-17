from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', HomePage, name='home'),
    path('category/<slug:slug>/', category_view, name='category'),
    path('<int:year>/<int:month>/<slug:slug>', Post_detail, name='post_detail'),
    path('author/<int:pk>/', author_view, name='author'),
]