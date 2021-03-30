from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return render(request,'index.html')
    return HttpResponse('<h1>Hello World</h1><hr><marquee style="color: red;font-size: 40px">Working Project</marquee>')
    