from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/%Y/%m/%d/', default='', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique_with=['published__month'],)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    # category = models.ManyToManyField(Category)
    created_by = models.ForeignKey(Author, on_delete=models.PROTECT, default=1)
    thumbnail = models.ImageField(upload_to='images/blog/%Y/%m/%d/', null=True, blank=True)
    body = models.TextField()
    # tag = 
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['published',]

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])
    
    def get_update_url(self):
        return reverse('blog:update-post', args=[self.slug])
    
    def get_delete_url(self):
        return reverse('blog:delete-post', args=[self.slug])

    def __str__(self):
        return self.title