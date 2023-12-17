from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse


from tinymce.models import HTMLField

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    overview = models.TextField()
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # comment_count = models.IntegerField(default=0)
    # view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False, null=True)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, null=True, blank=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, null=True, blank=True)


    # class Meta:
    #     # order on primary key to make sure it's unique
    #     ordering = ('timestamp', 'title', 'pk')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })
    
    def get_update_url(self):
        return reverse('post-update', kwargs={
            'id': self.id
        })
    
    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'id': self.id
        })
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
    
    @property
    def get_comment_count(self):
        return Comment.objects.filter(post=self).count()


    @property
    def get_view_count(self):
        return PostView.objects.filter(post=self).count()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username