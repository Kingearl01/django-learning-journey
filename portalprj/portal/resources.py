from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import *

class StudentResource(resources.ModelResource):
    user = fields.Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(User, field='username')
    )
    class Meta:
        model = Student
        fields = ['id','user','student_id', 'level', 'major', 'phone', 'year_admitted']
        export_order = ['id','user', 'student_id', 'level', 'major', 'phone', 'year_admitted']

class ResultResource(resources.ModelResource):
    course = fields.Field(
        column_name='course',
        attribute='course',
        widget=ForeignKeyWidget(Course, field='course_code')
    )

    student = fields.Field(
        column_name='student',
        attribute='student',
        widget=ForeignKeyWidget(Student, field='student_id')
    )

    class Meta:
        model = Result

        fields = ['id','student','course', 'grade',]
        export_order = ['id','student','course', 'grade',]


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        fields = ['id','course_code', 'course_title', 'credit', 'year', 'semester']
        export_order = ['id','course_code', 'course_title', 'semester', 'year', 'credit']
