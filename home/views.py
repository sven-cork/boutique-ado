from django.shortcuts import render

# Create your views here.

""" View to return the index page"""
def index(request):
    return render(request, 'home/index.html')