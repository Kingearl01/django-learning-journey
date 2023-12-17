from django.urls import reverse
from django.utils.html import mark_safe
from userauths.models import User

from django.db import models

# 3rd party
from shortuuid.django_fields import ShortUUIDField
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
def user_directory_path(instance, filename):
    return 'user {0}/{1}'.format(instance.user.id, filename)

STATUS_CHOICES = (
    ('process', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)


STATUS = (
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in_review', 'In Review'),
    ('published', 'published'),
)

RATING = (
    (1, '❤️💔💔💔💔'),
    (2, '❤️❤️💔💔💔'),
    (3, '❤️❤️❤️💔💔'),
    (4, '❤️❤️❤️❤️💔'),
    (5, '❤️❤️❤️❤️❤️'),
)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat', alphabet='abcdefgh12345')
    title = models.CharField(max_length=100, default='Food')
    image = models.ImageField(upload_to='category', default='category.jpg')


    class Meta:
        verbose_name_plural = 'Categories'

    def category_image(self):
        return mark_safe("<img src='%s' width='50', height='50'/>" % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_category_product_list_url(self):
        return reverse('core:category-product-list', args=[self.cid])

# class Tag(models.Model):
#     title = models.CharField(max_length=50,null=True, blank=True)
#     name = models.SlugField()

#     def __str__(self):
#         return self.title

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='ven', alphabet='abcdefgh12345')
   
    title = models.CharField(max_length=100, default='Nestify')
    image = models.ImageField(upload_to=user_directory_path, default='vendor.jpg')
    cover_image = models.ImageField(upload_to=user_directory_path, default='cover_image.jpg')
    description = RichTextUploadingField(null=True, blank=True, default='I"m amazing Vendor')

    address = models.CharField(max_length=100, default='123 , Main Street.')
    contact = models.CharField(max_length=100, default='+233 (123) 3455')
    chat_resp_time = models.CharField(max_length=100, default='100')
    ship_on_time = models.CharField(max_length=100, default='100')
    authentic_ratings = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    warranty_period = models.CharField(max_length=100, default='100')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'verdors'

    def vendor_image(self):
        return mark_safe("<img src='%s' width='50', height='50'/>" % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_vendor_url(self):
        return reverse('core:vendor-details', args=[self.vid])
    

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet='abcdefgh12345')
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name='vendor')

    title = models.CharField(max_length=100, default='Fresh Pear')
    image = models.ImageField(upload_to=user_directory_path, default='product.jpg')
    description = RichTextUploadingField( null=True, blank=True, default='his is specification')
    
    price = models.DecimalField(max_digits=99999999, decimal_places=2, default=1.99)
    old_price = models.DecimalField(max_digits=99999999, decimal_places=2, default=2.99)

    specifications = RichTextUploadingField( null=True, blank=True, default='It is specidication')
    tags = TaggableManager(blank=True)


    type = models.CharField(max_length=100, default='Organic')
    stock_count = models.PositiveIntegerField(default=10)
    expire_date = models.DateTimeField(auto_now_add=False)
    manufac_date = models.DateTimeField(auto_now_add=False)

    product_status = models.CharField(choices=STATUS, max_length=10, default='in_review')

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=20,prefix='sku', alphabet='1234567890')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'

    def product_image(self):
        return mark_safe("<img src='%s' width='50', height='50'/>" % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    
    def get_expire_date(self):
        return (self.expire_date - self.manufac_date)
    
    def get_product_url(self):
        return reverse('core:product-details', args=[self.pid])

class ProductImages(models.Model):
    images = models.ImageField(upload_to='product-images', default='product.jpg')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Images'

######################## Cart, Order, OrderItems and Address
######################## Cart, Order, OrderItems and Address
######################## Cart, Order, OrderItems and Address
######################## Cart, Order, OrderItems and Address

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=99999999, decimal_places=2, default=1.99)
    paid_status = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICES, max_length=30, default='processing')


    class Meta:
        verbose_name_plural = 'Cart Order'

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=99999999, decimal_places=2, default=1.99)
    total = models.DecimalField(max_digits=99999999, decimal_places=2, default=1.99)

    class Meta:
            verbose_name_plural = 'Cart Order Items'
    
    def order_img(self):
        return mark_safe("<img src='/media/%s' width='50', height='50'/>" % (self.image))
    

######################## Product Review, wishlist, Address
######################## Product Review, wishlist, Address
######################## Product Review, wishlist, Address
######################## Product Review, wishlist, Address


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    ratings = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return self.product.title
    
    def get_ratings(self):
        return self.ratings
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wishlist'

    def __str__(self):
        return self.product.title


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return self.address
