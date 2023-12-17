from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model managers where student ID is the unique identifiers
    for authentication instead of username
    """
    def create_user(self, student_id , password, **extra_fields):
        """
        create and save a user with the given student id and password.
        """

        if not student_id:
            raise ValueError(_("The Student ID must be set"))
        user = self.model(student_id=student_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self,student_id, password,  **extra_fields):
        """
        Create and save a superuser with the given email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(student_id, password, **extra_fields)