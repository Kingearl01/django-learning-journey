from django.contrib import admin

from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','category', 'date_created']
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','date_created']
    
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)