from django.http import HttpResponse


def about_us(request):
    return HttpResponse("Welcome to WscubeTech")


def course(request):
    return HttpResponse("Our Courses")
