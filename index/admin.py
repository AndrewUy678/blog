from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')

@admin.register(NewWork)
class NewWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file', 'time_create_work')



