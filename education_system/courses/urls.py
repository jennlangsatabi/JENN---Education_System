from django.urls import path
from .views import course_list, student_list

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('students/', student_list, name='student_list'),
]
