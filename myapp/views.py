from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect

def fun(request):
    return HttpResponse('<h1> Druga the mass</h1>')

def index(request):
    return HttpResponse('Hello,world. This is my project')
"""Dict only allowed to pass as aruments"""
def my_view(request):
    a={"title":"pthon"}
    return render(request,'index.html',a)