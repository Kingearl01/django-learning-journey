from django.urls import path

from store.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('update_item/', updateItem, name='update-item'),
    path('process_order/', processOrder, name='process-order'),
]