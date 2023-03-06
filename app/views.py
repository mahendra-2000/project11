from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vijji(request):
    return HttpResponse('<h1>Dont call me Akka</h1>')
def jeevitha(request):
    return HttpResponse('<h1>Dont call me Sis</h1>')
def mahi(request):
    return HttpResponse('<h1>Dont call me Bro</h1>')