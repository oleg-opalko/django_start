from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def start_app2(request):
    return HttpResponse('<h1>Hello App 2</h1>')
