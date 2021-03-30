from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return render(request,'index.html')
    return HttpResponse('<h1 style="font-family:aerial;">Hello World</h1><marquee>!!!Project working!!!</marquee>')
    
