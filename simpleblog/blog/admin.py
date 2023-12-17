from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'published', 'updated',]
    list_filter = ['updated','published','created_by' ]
    search_fields = ['title', 'body']
    # prepopulated_fields = {'slug': ('title',)}


