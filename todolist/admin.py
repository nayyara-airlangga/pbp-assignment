from django.contrib import admin

from todolist.models import Task

# Register your models here.
@admin.register(Task)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description', 'user')
