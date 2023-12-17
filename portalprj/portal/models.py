from django.db import models

from account.models import User
# Create your models here.

class Course(models.Model):
    LEVEL = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
    )
    SEMESTER = (
        ('1', '1'),
        ('2', '2'),
        
        
    )

    PROGRAMME = (
        ('BED. EARLY CHILDHOOD', 'EARLY CHILDHOOD'),
        ('BED. UPPER PRIMARY', 'UPPER PRIMARY'),
        ('BED. JHS', 'BED. JHS')
        
    )
    course_code = models.CharField(max_length=7, unique=True)
    course_title = models.CharField(max_length=250, unique=True)
    credit = models.PositiveSmallIntegerField()
    year = models.CharField(max_length=3, choices=LEVEL)
    semester = models.CharField(max_length=2, choices=SEMESTER)

    def __str__(self):
        return self.course_code

class Student(models.Model):
    LEVEL = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
    )

    MAJOR = (
         ('EARLY CHILDHOOD','EARLY CHILDHOOD'),
          ('PRIMARY EDUCATION','PRIMARY EDUCATION'),
        ('AGRICULTURAL SCIENCE', 'AGRIC'), 
        ('HOME ECONOMICS','H.ECONS'), 
        ('INFORMATION AND COMMUNICATION TECHNOLOGY','ICT'),
        ('INTERGRATED SCIENCE','INT.SCI'),
        ('MATHEMATICS','MATHS'), 
        ('RELIGIOUS AND MORAL EDUCATION','RME'),
        ('SOCIAL STUDIES','SOC.STUD'),
        ('TECHNICAL','TECHNICAL'),
         ('VISUAL ARTS','V.ARTS'),
        
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=12, unique=True)
    level = models.CharField(max_length=3, choices=LEVEL)
    major = models.CharField(max_length=50,choices=MAJOR)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    year_admitted = models.DateField()
 

    def __str__(self):
        return self.student_id
    
    

class Result(models.Model):
    GRADE = (
        ('4.0', 'A'),
        ('3.5', 'B+'),
        ('3.0','B'),
        ('2.5','C+'),
        ('2.0', 'C'),
        ('1.5', 'D+'),
        ('1.0', 'D'),
        ('0.5', 'E'),
        ('0.0', 'F'),
        ('IC', "IC"),
    )
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=4, choices=GRADE, )

    class Meta:
        unique_together = (('student', 'course'),)

    @property
    def calculate_total_credit(self):
        results = Result.objects.filter(student=self)

        total_credit = 0

        for result in results:
            total_credit += result.course.credit

        return total_credit

    def __str__(self):
        return f"{self.student} {self.grade} in {self.course.course_title}"

