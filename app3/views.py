from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second(request):
    return HttpResponse('<h2>Django is the one of the most beautiful and different subject in the fullstack development</h1>')

