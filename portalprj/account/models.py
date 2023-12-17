from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager
# # Create your models here.
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='user', null=True, blank=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     student_id = models.CharField('Student ID', max_length=11, unique=True)
#     first_name = models.CharField(max_length=15, null=True, blank=True)
#     last_name = models.CharField(max_length=15, null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     # username = None #Remove username, using email instead
#     # updated_at = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'student_id'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

    
#     def get_level(self):
#         level = self.date_joined.date
#         return level

#     def __str__(self):
#         return self.student_id


# # class User(AbstractUser):
#     # email = models.EmailField(unique=True)
#     # username = models.CharField(max_length=75, unique=True)
#     # bio = models.CharField(max_length=200, default="I'm moltivated Full stack developer")

#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = ['username']

#     # def __str__(self):
#     #     return self.username