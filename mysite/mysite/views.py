from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "index.html")


def about_us(request):
    return HttpResponse("Welcome to WscubeTech")


def course(request):
    return HttpResponse("Our Courses")


def course_details(request, courseid):
    return HttpResponse("Our Courses " + str(courseid))
