from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

def hello_world(resquest):
    return HttpResponse('hello world')
