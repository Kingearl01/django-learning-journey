from django.contrib import admin

from .models import *
from .resources import UserResource

from import_export.admin import ImportExportModelAdmin
# Register your models here.
class UserAdmin(ImportExportModelAdmin):
    resource_classes = [UserResource]
    list_display = ['username', 'user_type',]
admin.site.register(CustomUser, UserAdmin)