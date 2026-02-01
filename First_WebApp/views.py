from django import http
from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    return render(request,'index.html')
def hello (request):
    age=request.GET.get('user_age')
    name = request.GET.get('user_name')
    message= name +" "+age
    return render(request,'hello.html',{'message':message})
# def home(request):
#     return HttpResponse("Hello!\n This is the home page")
# def about(request):
#     return HttpResponse("Hello!\n This is the about page")
# def contact(request):
#     return HttpResponse("Hello!\n This is the contact page")