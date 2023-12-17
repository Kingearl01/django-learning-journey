from django.contrib import admin

from .resources import CustomUserResource

from .models import User
# # 3rd party
from import_export.admin import ImportExportModelAdmin

# # Register your models here.
class CustomUserAdmin(ImportExportModelAdmin):
    model = User
    list_display = ('username','first_name', 'last_name',)
    list_filter = ('username',)


    ordering = ("username",)
    resource_classes = [CustomUserResource]

admin.site.register(User, CustomUserAdmin)

