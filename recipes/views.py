from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', context={
        'name': 'Igor Gabriel'
    })

def contato(request):
    return render(request, 'temp.html')

def sobre(request):
    return HttpResponse('Sobre 3')
