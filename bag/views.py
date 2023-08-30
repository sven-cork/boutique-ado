from django.shortcuts import render

# Create your views here.

""" View to return the bag"""
def view_bag(request):
    return render(request, 'bag/bag.html')