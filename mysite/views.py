from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello_world(resquest):
    return HttpResponse('hello world')
