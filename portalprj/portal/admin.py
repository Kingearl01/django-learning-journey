from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import *
from .resources import *

# # Register your models here.
class StudentAdmin(ImportExportModelAdmin):
    resource_classes = [StudentResource]

    list_display = ('student_id', 'level', 'major', 'phone', 'year_admitted')
    list_filter = ('student_id', 'level', 'major', 'phone',)

class CourseAdmin(ImportExportModelAdmin):
    resource_classes = [CourseResource]

    list_display = ['course_code', 'course_title', 'credit', 'year', 'semester']
    list_filter = ['course_code', 'course_title',]
    ordering = ['year', 'semester']

class ResultAdmin(ImportExportModelAdmin):
    resource_classes = [ResultResource]

    list_display = ['student', 'course', 'grade']
    list_filter = ['student', 'course',]

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Result, ResultAdmin)