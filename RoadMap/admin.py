from django.contrib import admin
from .models import Major, Course, Map

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['members']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'major', 'semester']
    list_filter = ['major', 'semester']

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ['major', 'course', 'weeks_summary']
    list_filter = ['major', 'course', 'course__semester']
    search_fields = ['major__name', 'course__name']

    def weeks_summary(self, obj):
        weeks = obj.weeks
        if not weeks:
            return "No weeks"
        week_count = len(weeks)
        return f"{week_count} weeks"
    weeks_summary.short_description = 'Weeks'