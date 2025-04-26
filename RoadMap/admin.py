from django.contrib import admin
from .models import Major, Course

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['members']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'major', 'semester']
    list_filter = ['major', 'semester']