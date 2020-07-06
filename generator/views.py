from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    passwordCharcters = list('')
    isEmpty = True

    try:
        length = int(request.GET.get('length'))
    except:
        length = 8

    thePassword = ''

    if request.GET.get('uppercase'):
        passwordCharcters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        isEmpty = False

    if request.GET.get('lowercase'):
        passwordCharcters.extend(list('abcdefghijklmnopqrstuvwxyz'))
        isEmpty = False

    if request.GET.get('special'):
        passwordCharcters.extend(list('~!@#$%^&*()_+?'))
        isEmpty = False

    if request.GET.get('numbers'):
        passwordCharcters.extend(list('1234567890'))
        isEmpty = False

    if isEmpty:
        passwordCharcters.extend(list('abcdefghijklmnopqrstuvwxyz'))       

    for characters in range(length):
        thePassword += random.choice(passwordCharcters)

    return render(request, 'generator/password.html', {'password':thePassword})

def about(request):
    return render(request, 'generator/about.html')
