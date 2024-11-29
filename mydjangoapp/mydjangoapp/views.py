from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")
    return render(request, 'myapp/myapp.html')

def about(request):
    return render(request, 'websites/about.html')

def contact(request):
    return render(request, 'websites/contact.html')