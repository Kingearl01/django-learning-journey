from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    STU_LEVEL = (
        ('100', 100),
        ('200', 200),
        ('300', 300),
        ('400', 400)
        )
    
    # index_number = models.CharField(max_length=10, primary_key=True, blank=False, null=False)
    index_number = models.ForeignKey(User, on_delete=models.CASCADE, max_length=9)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    level = models.CharField(max_length=3, null=False, choices=STU_LEVEL)


    def __str__(self):
        return str(self.index_number)
    

class Course(models.Model):
    CREDITHOURS = (
        ('1', 4.0),('3', '3'),('6', '6'),('9', '9'),('12', '12')
    )
    code = models.CharField(max_length=6, null=True, blank=True)
    title = models.CharField(max_length=300, unique=True)
    credithours = models.CharField(max_length=2, default=3, choices=CREDITHOURS)
    # description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title


class Result(models.Model):
    GRADE = (('A', 'A'),('B+', 'B+'),('6', '6'),('9', '9'),('12', '12'))
    indexnumber = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, default='200048402')
    title = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True)
    grade = models.CharField(max_length=2, choices=GRADE)


    def __str__(self):
        return str(self.indexnumber) + " " + self.grade
