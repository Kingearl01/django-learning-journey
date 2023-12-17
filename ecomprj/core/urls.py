from django.urls import path

from .views import *

app_name = 'core'

urlpatterns = [
    # hoem
    path("", IndexView, name="index"),

    # PRODUCT
    path("products/", product_list_view, name="product-list"),
    path("product/<str:pid>/", product_detail_view, name="product-details"),

#   CATEGORY
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>", category_product_list_view, name="category-product-list"),
    
    # VENDOR
    path("vendors/", vendor_list_view, name="vendors"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-details"),


    # Tags
    path('products/tag/<slug:tag_slug>/', tag_list, name='tags'),

    # Reviews
    path('ajax-add-review/<str:pid>/', ajax_add_review, name='ajax-add-review'),

    # filter
    path('filter-products/', filter_product, name='filter-products'),

    path('add-to-cart/', add_to_cart, name="add-to-cart"),
]


