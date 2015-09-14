from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hi hi hiya earth! <br/> <a href='/rango/about'>About</a>")


def about(request):
    return HttpResponse("Rango says here is the about page -_-")