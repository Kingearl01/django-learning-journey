from django.contrib import admin

from core.models import *
# Register your models here.
class ProductImageAdmin(admin.TabularInline):
    model  = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines  = [ProductImageAdmin]
    list_display = ['pid','user', 'title','category','vendor', 'product_image', 'featured', 'price', 'product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image',]

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image',]

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price','paid_status', 'order_date', 'product_status']

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no','item', 'image', 'qty', 'price', 'total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','review', 'ratings']


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','date',]

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address','status', ]


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', ]
    prepopulated_fields = {'name': ('title',) }



admin.site.register(Vendor, VendorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
# admin.site.register(ProductImages, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)