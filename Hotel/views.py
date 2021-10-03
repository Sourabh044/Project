from django.shortcuts import render
from django.http import HttpResponse


def Hotel(request):
    return render(request,'MAIN.html')

def Signup(request):
    return render(request, 'Hotel/Single.html')