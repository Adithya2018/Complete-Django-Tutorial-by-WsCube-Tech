from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    data = {
        'title': 'Home Page',
        'bdata': 'Welcome to WsCubeTech',
        'clist': ['PHP', 'Java', 'C', 'Django'],
        'student_details': [
            {'name': 'Adi', 'phone': 244355},
            {'name': 'SDR', 'phone': 323224}
        ],
        'numbers': [10, 20, 30, 40, 50]
    }
    return render(request, "index.html", data)


def about_us(request):
    return HttpResponse("Welcome to WscubeTech")


def course(request):
    return HttpResponse("Our Courses")


def course_details(request, courseid):
    return HttpResponse("Our Courses " + str(courseid))
