from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# 3rd party
from taggit.managers import TaggableManager
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Author(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    description = models.TextField(default="You should write because you love the shape of stories and sentences andthe creation of different words on a page. Writing comes from reading, and reading is the finest teacher of how to write.")
    profile_pic = models.ImageField(upload_to='authors/', null=True, blank=True)

    @property
    def get_author_url(self):
        return reverse('blog:author', kwargs={'pk': self.id})
    
    @property
    def imageURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name')
   

    @property
    def get_category_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})
        

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with=('date_created','category'), max_length=500)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT, related_name='category')
    # description = models.TextField(null=True, blank=True)
    body = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='blog/images/%Y/%m/', default='blog/images/blog0.svg')
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)
    tags = TaggableManager(related_name='tags')
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0, blank=True, null=True)

    @property
    def get_absolute_url(self):
        year = self.date_created.year
        month = self.date_created.month
        return reverse('blog:post_detail', kwargs={'year': year, 'month': month, 'slug': self.slug})

    def __str__(self):
        return self.title
