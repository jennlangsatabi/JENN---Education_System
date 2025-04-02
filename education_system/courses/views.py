
from django.shortcuts import render
from .models import Course, Student

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'courses/student_list.html', {'students': students})
