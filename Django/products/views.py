from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request):
    return render(request,"index.html", {});

def product_view(request):
    return HttpResponse("<h1>project</h1>");

def contact_view(request):
    return HttpResponse("<h1>contact</h1>");

def about_view(request):
    return HttpResponse("<h1>about</h1>");