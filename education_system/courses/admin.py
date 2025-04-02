from django.contrib import admin
from .models import Course, Student

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'start_date', 'end_date')
    list_filter = ('instructor', 'start_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'display_courses')
    search_fields = ('name', 'email')
    filter_horizontal = ('enrolled_courses',)

    def display_courses(self, obj):
        return ", ".join([course.title for course in obj.enrolled_courses.all()])
    display_courses.short_description = 'Enrolled Courses'

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
