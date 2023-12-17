from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

intro = "Zoner Photo Studio X 19 Free Download Latest Version for Windows. The program and all files are checked and installed manually before uploading, program is working perfectly fine without any problem. It is full offline installer standalone setup of Zoner Photo Studio X 19 Free Download for supported version of Windows."
class Software(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(default=intro, null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_post = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title